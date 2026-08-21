# Contribuindo com o Fursec

Obrigado por querer ajudar. O Fursec é um catálogo curado — o valor dele está no que **não** entra, tanto quanto no que entra.

---

## Os três critérios

Toda sugestão de curso, livro, lab ou canal precisa passar por estes três:

1. **Gratuito de verdade.** Ou com uma camada gratuita substancial — e marcada como tal. "Grátis por 7 dias" não é gratuito. "Grátis para assistir, pago para o certificado" é, desde que a tag diga isso.
2. **Nada de material pirateado.** Todo link gratuito tem que ser distribuição autorizada pelo autor ou pela instituição. Se você não consegue apontar onde o autor liberou, não entra.
3. **Conteúdo em português é especialmente bem-vindo.** É onde a área tem menos material bom e organizado — e é o motivo de este repositório existir em PT-BR.

---

## Como adicionar uma linha

Os catálogos são tabelas markdown. Copie o formato do arquivo em que você está mexendo — ele varia por pasta.

**`cursos/*.md`** — 4 colunas:

```markdown
| Nome do curso | [Provedor](https://example.com/cursos/nome-do-curso) | 🇧🇷 | 🆓 🎓 |
```

**`labs/blue-team.md` e `labs/red-team-ctf.md`** — 4 colunas, com nota:

```markdown
| [Nome da plataforma](https://example.com/) | 🇺🇸 | 🆓 tier 🧪 | Uma linha dizendo o que a torna útil |
```

### Legenda das tags

| Tag | Significa |
|---|---|
| `🇧🇷` / `🇺🇸` | Idioma do conteúdo. Use os dois se houver legenda ou versão dublada. |
| `🆓` | Gratuito |
| `💸` | Pago |
| `🎓` | Emite certificado ou badge |
| `🧪` | Prático (lab, CTF, ambiente hands-on) |
| `⭐` | Prioridade alta — use com parcimônia, é o que a pessoa faz primeiro |

Qualificadores que acompanham o `🆓` quando a gratuidade tem ressalva: `parcial`, `tier`, `audit`, `via Financial Aid`.

### Regras de link

- **Aponte para a página do curso, não para a home do provedor.** `provedor.com/cursos/nome-do-curso` em vez de `provedor.com`. Um link genérico obriga a pessoa a caçar.
- **Sem texto de link genérico.** Nada de `[link]`, `[aqui]`, `[clique]` — use o nome do domínio ou do provedor.
- **Teste antes de mandar.** Muitos sites de curso devolvem 403 para automação; se o seu link cair nessa, diga no PR que você abriu no navegador e funcionou.
- **⭐ prioridade alta** é para o que você recomendaria a alguém com 5h por semana. Se tudo é prioridade, nada é.

---

## Verificação automática de links

Todo PR que toca em `.md` dispara a [verificação de links](.github/workflows/link-check.yml). Ela também roda toda segunda-feira e abre uma issue se algo quebrou.

Rate limit (429) e redirect de bot detection (307) são aceitos pelo próprio check — não precisam de exceção.

O [`.lycheeignore`](.lycheeignore) é só para hosts que **não dá para verificar**: aqueles que devolvem o mesmo resultado para um caminho válido e para um inventado, então nenhuma automação consegue distinguir link vivo de link morto. Antes de adicionar um host ali, meça o par: se o caminho inventado devolver 404, o host **é** verificável e não entra — colocá-lo na lista desligaria a única proteção que aquele host teria. Se entrar mesmo, escreva o comentário com a medição.

---

## Convenções de arquivo

Se você criar ou editar um arquivo `.md`:

- Começa com um `# H1` e um `[⬅️ Voltar ao índice](../README.md)` logo abaixo
- Termina com `---`, linha em branco, e o mesmo link de volta
- Réguas horizontais (`---`) sempre com linha em branco antes e depois
- Uma linha em branco no fim do arquivo, nunca duas
- Catálogos com coluna `Tags` levam a linha de legenda `<sub>` acima da primeira tabela

---

## Abrindo uma issue

- **Link quebrado ou curso que saiu do ar** → use o template de link quebrado. Diga o arquivo, a linha e o que você viu ao abrir.
- **Sugerir material novo** → use o template de sugestão. Ele pergunta pelos três critérios acima.

Se você já sabe qual é a correção, um PR é mais rápido que uma issue.

---

## O que provavelmente não entra

- Curso pago sem camada gratuita real (a exceção é [`livros/pagos.md`](livros/pagos.md) e a faixa paga de [`docs/certificacoes.md`](docs/certificacoes.md), que são explicitamente sobre gastar dinheiro)
- Conteúdo atrás de cadastro que exige CNPJ ou e-mail corporativo, sem alternativa
- Mais uma awesome-list genérica — [`repositorios/awesome-lists.md`](repositorios/awesome-lists.md) já cobre os índices mestres
- Ferramenta ofensiva sem contexto de uso legítimo e defensivo
