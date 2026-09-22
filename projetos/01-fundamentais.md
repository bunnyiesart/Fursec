# Projetos Fundamentais (P1–P4)

[← Voltar ao índice](../README.md)

---

Os quatro primeiros. Fazem parte da fase 0 e 1 do [roadmap](../ROADMAP.md) e não exigem trilha escolhida.

Todo projeto aqui segue a mesma estrutura: o que ele **prova**, quanto **tempo** leva, os **passos**, o **entregável**, e — o campo que mais importa — **como saber que está pronto**. Sem esse último, projeto vira gaveta.

> Leia [`00-regras.md`](./00-regras.md) antes de começar qualquer um.

---

### P1 — Home Lab documentado

**Prova que:** você constrói ambientes, não só consome tutorial.
**Tempo:** 8–15h · **Precisa de:** 8 GB de RAM e 100 GB livres ([nível 0 do home lab](../labs/home-lab.md) explica como fazer com menos)

**Passos:**
1. Instale o hypervisor — VirtualBox serve para começar, Proxmox se tiver máquina dedicada.
2. Suba as VMs: Kali, Ubuntu Server, Windows Server (licença de avaliação) e pfSense como roteador.
3. Segmente em VLANs e escreva **por que** você separou cada uma.
4. Documente cada problema que apareceu e como você resolveu.

**Entregável:** diagrama de rede, decisões de segmentação e o registro dos problemas.
**Pronto quando:** você consegue **destruir e reconstruir** o lab seguindo a sua própria documentação, sem consultar mais nada.
**Armadilha:** documentar só o que funcionou. O registro do que quebrou é o que prova experiência — e é o que você vai reler daqui a seis meses.
**Apoio:** [Ludus](https://github.com/badsectorlabs/ludus) (automação de lab) · [GOAD](https://github.com/Orange-Cyberdefense/GOAD) (lab de Active Directory)

---

### P2 — Analisador de força de senha (Python)

**Prova que:** programa, e entende entropia e ataque de força bruta.
**Tempo:** 4–6h · **Precisa de:** Python básico

**Passos:**
1. Calcule a **entropia real** da senha (tamanho × log₂ do alfabeto usado), não uma pontuação inventada.
2. Cheque contra lista de senhas vazadas — `rockyou.txt`, ou a [API do Have I Been Pwned](https://haveibeenpwned.com/API/v3) por k-anonimato.
3. Estime tempo de quebra para hardware real: offline com GPU, offline com CPU e online com limite de tentativa.
4. Devolva recomendação acionável, não só uma nota.

**Entregável:** script de linha de comando e um README explicando o modelo de ameaça de cada cenário.
**Pronto quando:** ele classifica corretamente `Senha@123` como fraca **apesar** de ter maiúscula, número e símbolo — e o seu README explica por quê.
**Armadilha:** confundir complexidade com força. Regra de composição é o que produz `P@ssw0rd!`; o que importa é tamanho e imprevisibilidade.
**Apoio:** [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html), seção de senhas — contradiz quase tudo que se ensinava

---

### P3 — Parser de logs em linha de comando

**Prova que:** automatiza análise, que é 80% do trabalho real.
**Tempo:** 5–8h · **Precisa de:** Python ou shell, e um log de verdade

**Passos:**
1. Leia `auth.log` do Linux ou o Event Log do Windows (evento 4625 = falha de logon).
2. Extraia tentativa falha: usuário, IP de origem, horário.
3. Agrupe por IP e por usuário, e conte.
4. Sinalize anomalia: muitas falhas do mesmo IP, uma falha em muitas contas (spraying), sucesso **logo depois** de várias falhas.
5. Saída legível por humano **e** em JSON, para encadear com outra ferramenta.

**Entregável:** o script, mais uma amostra de log e a saída correspondente.
**Pronto quando:** você aponta o script para um log que ele nunca viu e ele acha o padrão sem você ajustar nada.
**Armadilha:** contar só falha por IP. O ataque que importa hoje é o contrário — **uma** tentativa em muitas contas, que não estoura nenhum limiar por IP.
**Apoio:** gere log de teste atacando a sua própria VM do [P1](#p1--home-lab-documentado)

---

### P4 — Hardening baseline aplicado

**Prova que:** conhece controle de segurança na prática, e sabe medir o efeito.
**Tempo:** 6–10h · **Precisa de:** uma VM descartável do [P1](#p1--home-lab-documentado)

**Passos:**
1. Rode o [OpenSCAP](https://www.open-scap.org/) na VM **antes** de qualquer mudança e guarde o relatório.
2. Aplique um [CIS Benchmark](https://www.cisecurity.org/cis-benchmarks) do sistema, controle por controle.
3. Rode de novo e compare.
4. Para cada controle que você **não** aplicou, escreva o motivo — quebra de compatibilidade, custo operacional, risco aceito.

**Entregável:** relatório com o delta antes/depois e a lista justificada de exceções.
**Pronto quando:** você consegue defender cada exceção para alguém que pergunte "por que não aplicou este?".
**Armadilha:** aplicar o benchmark inteiro sem testar e deixar a máquina inoperante. Hardening que quebra o serviço é revertido na segunda-feira — e a lista de exceções justificadas vale mais que a pontuação.
**Apoio:** [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) · [OpenSCAP](https://www.open-scap.org/) · [Lynis](https://github.com/CISOfy/lynis) para uma segunda opinião

---

[← Voltar ao índice](../README.md)
