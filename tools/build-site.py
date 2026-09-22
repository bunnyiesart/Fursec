#!/usr/bin/env python3
"""Gera o site do Fursec em _site/.

Cada .md vira uma página HTML. A conversão de markdown não é feita aqui: o
HTML vem da própria API do GitHub (`Accept: application/vnd.github.html`), que
é o mesmo renderizador do repositório. Assim tabela, checkbox de tarefa, emoji
e âncora saem idênticos ao que a pessoa vê no GitHub, sem depender de uma
biblioteca de markdown que renderize diferente.

As URLs não levam .html: /projetos/05-grc e /trilhas/. Quem faz isso é o
GitHub Pages, que entrega /x.html para /x e /x/index.html para /x/. Os
arquivos no disco continuam .html — só os links deixam de mostrar a extensão.
Para conferir localmente é preciso um servidor com a mesma regra; o
`python3 -m http.server` resolve a pasta, mas não o /x sem extensão.

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
# Domínio próprio servido pelo Pages. Vazio = publica no endereço do GitHub.
DOMINIO = os.environ.get("FURSEC_DOMINIO", "furrsec.com")

# As seções que aparecem na lateral de toda página de documento, na ordem em
# que o índice as apresenta. A chave é a pasta, usada para marcar em qual
# seção a página atual está.
SECOES = [
    ("trilhas", "Trilhas", "trilhas/"),
    ("", "Roadmap", "ROADMAP"),
    ("cursos", "Cursos", "cursos/"),
    ("labs", "Labs", "labs/"),
    ("projetos", "Projetos", "projetos/"),
    ("repositorios", "Repositórios", "repositorios/"),
    ("livros", "Livros", "livros/"),
    ("docs", "Documentação", "docs/"),
    ("recursos", "Recursos", "recursos/"),
    ("progresso", "Progresso", "progresso/"),
]
API = f"https://api.github.com/repos/{REPO}/contents/"
# Ref a renderizar. Vazio = branch default do repositorio, que e o que a
# publicacao quer. Num pull request isso renderizaria a main em vez do PR,
# entao o CI passa o SHA do PR aqui — sem isso, conferir um PR e conferir
# o conteudo errado.
REF = os.environ.get("FURSEC_REF", "")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Não vira página: o índice do site já cumpre esse papel, e os artefatos de
# desenvolvimento (verdade de produto, design system, contrato de direção) são
# documentação do repositório, não conteúdo do site. Sem esta exclusão o build
# gera página para eles e o check-site acusa órfã, porque o índice — com razão
# — não linka nenhum deles.
IGNORAR = {"README.md", "PRODUCT.md", "DESIGN.md"}

# Pastas cujo .md nunca vira página.
FORA = (".github/", ".impeccable/")

# Emoji da legenda -> etiqueta escrita. A ordem importa: bandeira antes de
# qualquer coisa, e os pares de indicador regional antes dos isolados.
ETIQUETAS = [
    ("\U0001F1E7\U0001F1F7", "PT", ""),            # bandeira do Brasil
    ("\U0001F1FA\U0001F1F8", "EN", ""),            # bandeira dos EUA
    ("\U0001F193", "grátis", " tag--gratis"),      # 🆓
    ("\U0001F4B8", "pago", ""),                     # 💸
    ("\U0001F4B3", "pago", ""),                     # 💳
    ("\U0001F393", "cert", ""),              # 🎓
    ("\U0001F9EA", "lab", ""),                  # 🧪
    # ⭐ não entra aqui: virou peso no nome, em destaca_prioridade()  # ⭐
    ("\U0001F534", "crítico", " tag--prioridade"), # 🔴 risco
    ("\U0001F7E0", "alto", ""),                     # 🟠
    ("\U0001F7E1", "médio", ""),                    # 🟡
    ("\U0001F7E2", "baixo", ""),
    ("\u26AA", "a fazer", ""),             # ⚪ status a preencher                    # 🟢
]

# Emoji que só repete a palavra ao lado: "FAÇA", "NUNCA FAÇA",
# "Quase nunca", "Defensiva". Sai, e o texto continua dizendo tudo.
REMOVER = (
    "\u2B50",                                 # estrela solta fora de tabela
    "\u2705", "\u274C",                      # marca e cruz de polaridade
    "\u26A0\uFE0F", "\u26A0",                # aviso
    "\U0001F535", "\U0001F4CB",              # marcadores de trilha
    "\u2601\uFE0F", "\u2601",
    "\U0001F7E3", "\U0001F6E1\uFE0F", "\U0001F6E1",
)


def versionados():
    saida = subprocess.run(["git", "-C", RAIZ, "ls-files", "*.md"],
                           capture_output=True, text=True, check=True).stdout
    return sorted(f for f in saida.split()
                  if not f.startswith(FORA) and f not in IGNORAR)


def render(caminho, token):
    req = urllib.request.Request(
        API + caminho + (f"?ref={REF}" if REF else ""),
        headers={"Accept": "application/vnd.github.html",
                 "User-Agent": "fursec-build",
                 **({"Authorization": f"Bearer {token}"} if token else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def destino(caminho):
    """Arquivo no disco.

    O README de uma pasta vira o index.html dela, e é isso que faz a pasta
    ter endereço próprio: /trilhas/ em vez de /trilhas/README.html.
    """
    if caminho.endswith("/README.md"):
        return caminho[:-len("README.md")] + "index.html"
    return caminho[:-3] + ".html"


def url(arq):
    """Endereço público de um .md, sem extensão.

    O GitHub Pages serve /x quando existe /x.html, e /x/ quando existe
    /x/index.html. Então o .html no fim da URL é ruído: some daqui, e o
    arquivo no disco continua o mesmo.
    """
    if arq == "README.md":
        return "./"
    if arq.endswith("/README.md"):
        return arq[:-len("README.md")]
    return arq[:-3]


def fora_de_pre(html_, fn):
    """Aplica fn só no que está FORA de <pre>.

    Dentro de bloco de código o emoji é conteúdo: as árvores de diretório de
    docs/ usam 📁 e 📌 como parte do desenho, e trocá-los por etiqueta
    quebraria o exemplo.
    """
    partes = re.split(r"(<pre[\s\S]*?</pre>)", html_)
    return "".join(p if p.startswith("<pre") else fn(p) for p in partes)


def destaca_prioridade(trecho):
    """A estrela marcava "faça este primeiro". Vira negrito no nome.

    Como etiqueta ela ficava com mais peso visual que o curso que
    qualificava. Negrito é o eixo que esta página já usa para hierarquia,
    e dispensa legenda: o olho entende "comece por estes" sem decodificar.
    """
    return re.sub(
        r"<td>\s*\u2B50\s*(.*?)</td>",
        r'<td><strong class="prio" title="Prioridade alta">\1</strong></td>',
        trecho, flags=re.S)


def etiquetar(trecho):
    trecho = destaca_prioridade(trecho)
    for emoji, rotulo, classe in ETIQUETAS:
        trecho = trecho.replace(
            emoji, f'<span class="tag{classe}">{rotulo}</span>')
    for emoji in REMOVER:
        trecho = trecho.replace(emoji + " ", "").replace(emoji, "")
    return trecho


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

    # 3. Links entre documentos: .md -> URL sem extensão (ver url()).
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
                return f'href="{subir or "./"}{frag}"'
        if arq.endswith(".md"):
            return f'href="{url(arq)}{frag}"'
        resolvido = os.path.normpath(os.path.join(os.path.dirname(caminho), arq))
        # Link para pasta: no site quem faz esse papel é o README dela.
        if os.path.isdir(os.path.join(RAIZ, resolvido)) and \
           os.path.exists(os.path.join(RAIZ, resolvido, "README.md")):
            return f'href="{arq.rstrip("/")}/{frag}"'
        # Relativo para algo que não é .md nem pasta com índice (workflow,
        # .lycheeignore): não existe no site, então aponta para o GitHub.
        return f'href="https://github.com/{REPO}/blob/main/{resolvido}{frag}"'

    corpo = re.sub(r'href="([^"]+)"', link, corpo)

    # 4. Tabela larga precisa rolar sozinha, senão estoura a largura da página.
    corpo = corpo.replace("<table>", '<div class="table-wrap"><table>') \
                 .replace("</table>", "</table></div>")

    # 5. Tags: emoji viram etiqueta tipográfica.
    #
    #    A legenda (idioma, gratuidade, certificado, prático, prioridade) é
    #    dado que a pessoa filtra, e por isso fica. Mas emoji é a APRESENTAÇÃO
    #    errada dele: duas colunas coloridas em 36 linhas são a cara de
    #    catálogo gerado por máquina, e o design system proíbe emoji na
    #    interface. No GitHub o emoji funciona e continua no markdown; aqui o
    #    site usa a própria linguagem.
    corpo = fora_de_pre(corpo, etiquetar)

    # 6. A legenda das tags existia para decodificar o emoji. Com etiqueta
    #    escrita ela não decodifica nada, e repetia duas linhas em 12 páginas.
    corpo = re.sub(r"<sub>\s*(<span class=\"tag[^\n]*?)</sub>\s*", "", corpo)

    # 6b. O GitHub renderiza checkbox de tarefa desabilitado, porque lá ele
    #     é só leitura. Aqui o assets/doc.js os torna um checklist com estado
    #     salvo, então o disabled tem de sair.
    corpo = corpo.replace(
        ' disabled="" class="task-list-item-checkbox"',
        ' class="task-list-item-checkbox"')

    # 7. O markdown traz "Voltar ao índice" no topo e no pé, porque no
    #    GitHub não existe migalha. Aqui existe, então o do topo era o
    #    terceiro elemento de navegação seguido antes de qualquer conteúdo.
    #    O do pé fica: é o retorno natural no fim de um documento longo.
    corpo = re.sub(
        r'<p[^>]*>\s*<a href="[^"]*">\s*\u2190[^<]*</a>\s*</p>\s*',
        "", corpo, count=1)

    return corpo


def rotulo_curto(bruto):
    """Limpa o texto de um heading para caber na lateral.

    O checklist tem headings como "Fase 2 — Trilha primária: ______________",
    e os sublinhados de preenchimento viram um traço solto na lateral.
    """
    txt = re.sub(r"<[^>]+>", "", bruto)
    txt = re.sub(r"_{3,}", "", txt)          # campo de preencher à mão
    txt = re.sub(r"[\s:—-]+$", "", txt)      # pontuação que sobra no fim
    return re.sub(r"\s{2,}", " ", txt).strip()


def sumario_de(corpo):
    """Extrai os <h2> da página para o sumário da lateral.

    Só h2: h3 em documento longo como o home-lab daria uma lista de 39 itens,
    que deixa de ser sumário e passa a ser parede.
    """
    itens = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', corpo, re.S)
    if len(itens) < 2:
        return ""
    linhas = "".join(
        f'<li><a href="#{i}">{html.escape(rotulo_curto(txt))}</a></li>'
        for i, txt in itens)
    return ('<details class="sumario" open><summary>Nesta página</summary>'
            f'<ul>{linhas}</ul></details>')


def lateral_de(caminho, subir, corpo):
    """Monta a navegação lateral, com a seção atual marcada."""
    pasta = caminho.split("/")[0] if "/" in caminho else ""
    links = []
    for chave, rotulo, destino in SECOES:
        aqui = ' aria-current="true"' if chave == pasta else ""
        links.append(f'<li><a href="{subir}{destino}"{aqui}>{rotulo}</a></li>')
    return (
        f'<a class="marca" href="{subir or "./"}">Fursec</a>'
        f'<ul class="secoes">{"".join(links)}</ul>'
        + sumario_de(corpo))


LAYOUT = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} — Fursec</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><style>path{{fill:%2316171a}}@media(prefers-color-scheme:dark){{path{{fill:%23e7e8ea}}}}</style><path d='M8 14.6c-3.9 0-6.1-3-6.1-6.2V1.9l3.6 2.7A9 9 0 0 1 8 4.3c.9 0 1.7.1 2.5.3L14.1 1.9v6.5c0 3.2-2.2 6.2-6.1 6.2zm-2.2-6.9a.85.85 0 1 0 0 1.7.85.85 0 0 0 0-1.7zm4.4 0a.85.85 0 1 0 0 1.7.85.85 0 0 0 0-1.7zM8 10.8l-1.1 1.1h2.2z'/></svg>">
<link rel="stylesheet" href="{subir}assets/site.css">
</head>
<body class="doc">

<a class="pular" href="#conteudo">Pular para o conteúdo</a>

<div class="pagina">
<nav class="lateral" aria-label="Navegação do site">
{lateral}
</nav>

<main class="conteudo" id="conteudo">
<article class="md">
{corpo}
</article>
</main>
</div>

<script src="{subir}assets/doc.js" defer></script>
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
                lateral=lateral_de(caminho, "../" * caminho.count("/"), corpo),
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
        return f'href="{url(arq)}{"#" + frag if frag else ""}"'
    idx, n = re.subn(rf'href="({re.escape(prefixo)}[^"]+)"', local, idx)
    open(os.path.join(saida, "index.html"), "w", encoding="utf-8").write(idx)

    shutil.copytree(os.path.join(RAIZ, "assets"), os.path.join(saida, "assets"))
    open(os.path.join(saida, ".nojekyll"), "w").close()

    # Domínio próprio. A publicação por workflow guarda o domínio na
    # configuração do Pages, então este arquivo é cinto e suspensório: se a
    # configuração for perdida, o CNAME no artefato a restabelece. Um arquivo
    # a mais é mais barato que um site fora do ar por um dia.
    if DOMINIO:
        with open(os.path.join(saida, "CNAME"), "w", encoding="utf-8") as f:
            f.write(DOMINIO + "\n")

    print(f"{paginas} páginas + índice ({n} links locais) em {args.saida}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
