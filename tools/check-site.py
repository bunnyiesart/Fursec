#!/usr/bin/env python3
"""Confere os links internos do site gerado.

Não toca em link externo — disso cuida o workflow de verificação de links.
Aqui o alvo é o que o build pode quebrar sozinho: página que não existe e,
principalmente, âncora que aponta para um id inexistente. Âncora quebrada
devolve 200 e leva a pessoa para o topo em silêncio, então nenhum verificador
de status pega.

Uso:
    python3 tools/check-site.py [_site]
"""

import os
import re
import sys
import urllib.parse

HREF = re.compile(r'href="([^"]+)"')
ID = re.compile(r'id="([^"]+)"')


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else "_site"
    if not os.path.isdir(raiz):
        print(f"erro: {raiz}/ não existe — rode o build antes", file=sys.stderr)
        return 1

    paginas = [os.path.join(d, f)
               for d, _, fs in os.walk(raiz) for f in fs if f.endswith(".html")]
    if not paginas:
        print(f"erro: nenhuma página em {raiz}/", file=sys.stderr)
        return 1

    ids = {}
    for p in paginas:
        ids[os.path.normpath(p)] = set(ID.findall(open(p, encoding="utf-8").read()))

    problemas = []
    total = 0
    for p in paginas:
        base = os.path.dirname(p)
        for href in HREF.findall(open(p, encoding="utf-8").read()):
            if href.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            total += 1
            arq, _, frag = href.partition("#")
            alvo = (os.path.normpath(os.path.join(base, urllib.parse.unquote(arq)))
                    if arq else os.path.normpath(p))
            if not os.path.exists(alvo):
                problemas.append(f"{p}: página inexistente -> {href}")
            elif frag and frag not in ids.get(alvo, set()):
                problemas.append(f"{p}: âncora inexistente -> {href}")

    for x in problemas:
        print(f"::error::{x}")
    print(f"{total} links internos verificados em {len(paginas)} páginas; "
          f"{len(problemas)} quebrado(s)")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main())
