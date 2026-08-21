#!/usr/bin/env python3
"""Gera o site do Fursec em _site/.

Cada .md vira uma página HTML. A conversão de markdown não é feita aqui: o
HTML vem da própria API do GitHub (`Accept: application/vnd.github.html`), que
é o mesmo renderizador do repositório. Assim tabela, checkbox de tarefa, emoji
e âncora saem idênticos ao que a pessoa vê no GitHub, sem depender de uma
biblioteca de markdown que renderize diferente.

Uso:
    GITHUB_TOKEN=... python3 tools/build-site.py [--saida _site]
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "bunnyiesart/Fursec")
API = f"https://api.github.com/repos/{REPO}/contents/"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Não vira página: o índice do site já cumpre esse papel.
IGNORAR = {"README.md"}


def versionados():
    saida = subprocess.run(["git", "-C", RAIZ, "ls-files", "*.md"],
                           capture_output=True, text=True, check=True).stdout
    return sorted(f for f in saida.split()
                  if not f.startswith(".github/") and f not in IGNORAR)


def render(caminho, token):
    req = urllib.request.Request(
        API + caminho,
        headers={"Accept": "application/vnd.github.html",
                 "User-Agent": "fursec-build",
                 **({"Authorization": f"Bearer {token}"} if token else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def destino(caminho):
    return caminho[:-3] + ".html"


def reescreve(corpo, caminho):
    """Ajusta o HTML do GitHub para funcionar como página estática."""
    prof = caminho.count("/")
    subir = "../" * prof

    # 1. O id do cabeçalho fica num <a> depois dele, prefixado com
    #    "user-content-", enquanto os links apontam sem prefixo. No github.com
    #    um script concilia isso; numa página estática, não. Passa o id para o
    #    próprio cabeçalho e descarta o <a> do permalink.
    corpo = re.sub(
        r'<h([1-6]) class="heading-element"[^>]*>(.*?)</h\1>'
        r'<a id="user-content-([^"]+)"[^>]*>.*?</a>',
        lambda m: f'<h{m.group(1)} id="{m.group(3)}">{m.group(2)}</h{m.group(1)}>',
        corpo, flags=re.S)
    # 2. Sobram os ids de âncoras escritas à mão no markdown; mesmo prefixo.
    corpo = corpo.replace('id="user-content-', 'id="')

    # 3. Links entre documentos: .md -> .html. README.md é o índice do site.
    def link(m):
        alvo = m.group(1)
        if alvo.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        arq, _, frag = alvo.partition("#")
        frag = "#" + frag if frag else ""
        if arq.endswith("README.md") and arq.count("/") == alvo.count("/"):
            # "../README.md" a partir de qualquer pasta = índice do site
            base = os.path.normpath(os.path.join(os.path.dirname(caminho), arq))
            if base == "README.md":
                return f'href="{subir or "./"}index.html{frag}"'
        if arq.endswith(".md"):
            return f'href="{arq[:-3]}.html{frag}"'
        # Relativo para algo que não é .md (workflow, .lycheeignore, pasta):
        # esses arquivos não existem no site. Aponta para o GitHub, senão
        # viraria link quebrado.
        resolvido = os.path.normpath(os.path.join(os.path.dirname(caminho), arq))
        return f'href="https://github.com/{REPO}/blob/main/{resolvido}{frag}"'

    corpo = re.sub(r'href="([^"]+)"', link, corpo)

    # 4. Tabela larga precisa rolar sozinha, senão estoura a largura da página.
    corpo = corpo.replace("<table>", '<div class="table-wrap"><table>') \
                 .replace("</table>", "</table></div>")
    return corpo


LAYOUT = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} — Fursec</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><text y='14' font-size='14'>&#129418;</text></svg>">
<link rel="stylesheet" href="{subir}assets/site.css">
</head>
<body>

<p class="crumb"><a href="{subir}index.html">&lsaquo; Fursec</a></p>

<article class="md">
{corpo}
</article>

</body>
</html>
"""


def titulo_de(corpo, caminho):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", corpo, re.S)
    bruto = m.group(1) if m else os.path.basename(caminho)[:-3]
    return html.escape(re.sub(r"<[^>]+>", "", bruto).strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida", default="_site")
    args = ap.parse_args()
    saida = os.path.join(RAIZ, args.saida)
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    if os.path.isdir(saida):
        shutil.rmtree(saida)
    os.makedirs(saida)

    arquivos = versionados()
    paginas = 0
    for caminho in arquivos:
        try:
            bruto = render(caminho, token)
        except urllib.error.HTTPError as e:
            print(f"ERRO {e.code} ao renderizar {caminho}", file=sys.stderr)
            return 1
        corpo = reescreve(bruto, caminho)
        titulo = titulo_de(corpo, caminho)
        alvo = os.path.join(saida, destino(caminho))
        os.makedirs(os.path.dirname(alvo), exist_ok=True)
        with open(alvo, "w", encoding="utf-8") as f:
            f.write(LAYOUT.format(
                titulo=titulo,
                desc=f"{titulo} — trilha de cibersegurança com material gratuito.",
                subir="../" * caminho.count("/"),
                corpo=corpo))
        paginas += 1

    # Índice: os links apontam para o GitHub no fonte; no site apontam para as
    # páginas locais. O fonte continua útil aberto direto no repositório.
    idx = open(os.path.join(RAIZ, "index.html"), encoding="utf-8").read()
    prefixo = f"https://github.com/{REPO}/blob/main/"
    def local(m):
        alvo = m.group(1)[len(prefixo):]
        arq, _, frag = alvo.partition("#")
        if not arq.endswith(".md"):
            return m.group(0)
        return f'href="{arq[:-3]}.html{"#" + frag if frag else ""}"'
    idx, n = re.subn(rf'href="({re.escape(prefixo)}[^"]+)"', local, idx)
    open(os.path.join(saida, "index.html"), "w", encoding="utf-8").write(idx)

    shutil.copytree(os.path.join(RAIZ, "assets"), os.path.join(saida, "assets"))
    open(os.path.join(saida, ".nojekyll"), "w").close()

    print(f"{paginas} páginas + índice ({n} links locais) em {args.saida}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
