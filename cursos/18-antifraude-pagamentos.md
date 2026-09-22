# Antifraude e segurança em pagamentos

[← Voltar ao índice](../README.md)

---

A área com o maior descompasso entre demanda e gente formada no Brasil. O Pix processa bilhões de transações, o Banco Central endureceu a régua de controle antifraude, e cada instituição precisa provar de forma auditável que o controle dela funciona — o que gera vaga técnica que quase ninguém está estudando pra ocupar.

E é uma área onde o material bom é **norma e especificação**, não curso. Isso assusta no começo e depois vira vantagem: quem lê a fonte primária conversa de igual com o regulador e com o time de risco.

Pré-requisito honesto: faça [`01-introducao-seguranca.md`](./01-introducao-seguranca.md) antes, e tenha [`13-identidade.md`](./13-identidade.md) por perto — autenticação é metade do problema de fraude.

<sub>🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva</sub>

<sub>Esta página usa uma quinta coluna, **Nota**, que os arquivos 00–07 não têm. É
deliberado: são áreas de nicho em que o nome do item não diz o que ele é. O
formato segue o de [`labs/`](../labs/), que já usa nota.</sub>

| Curso / material | Fonte | Lang | Tags | Nota |
|---|---|---|---|---|
| ⭐ Manual de Segurança do SFN — Vol. II: Segurança do Pix | [bcb.gov.br](https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual%20de%20Seguran%C3%A7a%20do%20SFN%20-%20Vol.II%20-%20v6_00.pdf) | 🇧🇷 | 🆓 | O documento que define os requisitos técnicos de segurança do Pix: autenticação mútua, assinatura de mensagem, log de auditoria e rastreabilidade. É a fonte, não o resumo dela |
| ⭐ Regulamento do Pix | [bcb.gov.br](https://www.bcb.gov.br/estabilidadefinanceira/pix/regulamentopix) | 🇧🇷 | 🆓 | A regra em vigor, incluindo o mecanismo especial de devolução. Ler isto é o que separa quem opina de quem sabe o que a instituição é obrigada a fazer |
| Pix — página do Banco Central | [bcb.gov.br](https://www.bcb.gov.br/estabilidadefinanceira/pix) | 🇧🇷 | 🆓 | Ponto de entrada: estatística, manuais, guias e as mudanças de regra conforme saem |
| Open Finance Brasil — portal do desenvolvedor | [openfinancebrasil.atlassian.net](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/overview) | 🇧🇷 | 🆓 🧪 | Especificação viva de consentimento, FAPI e certificado. É onde se aprende OAuth de alta segurança com um caso real e brasileiro |
| ANPD — incidente de segurança com dado pessoal | [gov.br](https://www.gov.br/anpd/pt-br/assuntos/incidente-de-seguranca) | 🇧🇷 | 🆓 | Prazo e forma de comunicar vazamento. Fraude quase sempre vira incidente de dado pessoal, e é aqui que a obrigação começa |
| Cartilha de Segurança — CERT.br | [cartilha.cert.br](https://cartilha.cert.br/) | 🇧🇷 | 🆓 | Os fascículos de golpe são o melhor catálogo público de engenharia social aplicada ao brasileiro: falso funcionário, falso leilão, mão fantasma |
| ACFE — Free Training & Resources | [acfe.com](https://www.acfe.com/fraud-resources/free-training-and-resources) | 🇺🇸 | 🆓 | Material aberto da entidade de referência em investigação de fraude, incluindo o Fraud Risk Management Guide feito com o COSO |
| PCI SSC — Document Library | [pcisecuritystandards.org](https://www.pcisecuritystandards.org/document_library/) | 🇺🇸 | 🆓 | PCI DSS e os guias suplementares, de graça. Obrigatório se o assunto for cartão |
| FIDO2 e passkeys | [fidoalliance.org](https://fidoalliance.org/fido2/) | 🇺🇸 | 🆓 | A especificação que está matando o phishing de credencial. Entender isto é o caminho mais direto pra reduzir fraude de tomada de conta |
| Credit Card Fraud Detection (dataset) | [kaggle.com](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) | 🇺🇸 | 🆓 🧪 | Dados reais e anonimizados pra treinar detecção. O exercício de verdade aqui é lidar com classe desbalanceada, que é o problema central de antifraude |
| ACAMS — certificados antifraude (CAFS) | [acams.org](https://www.acams.org/en/training/acams-certificates) | 🇺🇸 | 💸 🎓 | A sigla que o mercado financeiro reconhece. Caro, e não é porta de entrada: só faz sentido quando você já trabalha na área |

---

## Como estudar isto sem trabalhar num banco

O problema da área é que você não tem acesso à base de transação. Três formas de contornar:

1. **Construa o detector com o dataset do Kaggle.** Classe desbalanceada, custo assimétrico de erro (bloquear cliente bom custa diferente de deixar passar fraude) e métrica que não seja acurácia. Isso é o trabalho real.
2. **Leia o Manual de Segurança do Pix e escreva o que faltaria no seu projeto.** Pegue o [P32](../projetos/06-appsec.md#p32--pipeline-cicd-com-segurança-embutida) e liste quais requisitos do manual o pipeline dele atenderia.
3. **Modele a fraude como ameaça.** O [P31](../projetos/06-appsec.md#p31--threat-model-de-um-projeto-open-source) com STRIDE aplicado a um fluxo de pagamento fictício é um portfólio que quase ninguém tem.

---

[← Voltar ao índice](../README.md)
