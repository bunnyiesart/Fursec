# 🏠 Home Lab Barato — Guia Completo

[⬅️ Voltar ao índice](../README.md)

---

O home lab é o **projeto P1** e a base de todo o resto. A boa notícia: dá para começar hoje com **R$ 0**. A má notícia que ninguém conta: o limite não é o processador — é **RAM**. Todo o resto deste guia gira em torno disso.

---

## Escolha seu nível

| Nível | Custo | O que dá para fazer | Para quem |
|---|---|---|---|
| **0 — Notebook que você já tem** | R$ 0 | 2–3 VMs, fundamentos, web hacking, CTF | Todo mundo começa aqui |
| **0.5 — Nuvem gratuita** | R$ 0 | Servidor Linux 24/7, honeypot, SIEM leve | Complementa o nível 0 |
| **1 — Mini PC usado** | ~US$ 80–180 | 5–8 VMs, lab de AD, SIEM completo | Quando o notebook travar |
| **2 — Upgrade de RAM** | ~US$ 30–60 | 10+ VMs, GOAD, malware analysis | Quando 16 GB acabar |

> **Não pule direto para o nível 1.** Passe pelo menos 2 meses no nível 0. Muita gente compra hardware e nunca usa — o gargalo quase sempre é tempo, não máquina.

---

## 🆓 Nível 0 — Custo zero (comece aqui)

### O que você precisa

| Item | Mínimo | Confortável |
|---|---|---|
| RAM | 8 GB | 16 GB |
| Disco livre | 100 GB | 250 GB (SSD) |
| CPU | 4 threads com virtualização | 8 threads |
| Sistema | Qualquer (Win/Mac/Linux) | — |

**Verifique se a virtualização está ligada.** É o erro nº 1 de quem começa — a VM não liga e a pessoa acha que o PC é fraco.

```bash
# Linux
grep -E --color 'vmx|svm' /proc/cpuinfo | head -1

# macOS
sysctl -a | grep machdep.cpu.features | grep VMX

# Windows (PowerShell) — procure "Virtualization Enabled In Firmware: Yes"
systeminfo | Select-String "Hyper-V|Virtualization"
```

Se estiver desativada, ligue na BIOS/UEFI: `Intel VT-x` / `AMD-V` ou `SVM Mode`.

### Software (tudo gratuito)

| Ferramenta | Para quê | Link |
|---|---|---|
| **VirtualBox** | Hypervisor — o mais simples para começar | [virtualbox.org](https://www.virtualbox.org/) |
| VMware Workstation Player | Alternativa, gratuito para uso pessoal | [broadcom.com](https://www.vmware.com/) |
| UTM | Melhor opção para Mac com chip Apple (ARM) | [mac.getutm.app](https://mac.getutm.app/) |

### Sistemas operacionais gratuitos e legais

| ISO | Custo | Onde |
|---|---|---|
| Kali Linux (imagens prontas para VM) | Grátis | [kali.org](https://www.kali.org/get-kali/#kali-virtual-machines) |
| Ubuntu Server | Grátis | [ubuntu.com](https://ubuntu.com/download/server) |
| Windows Server — avaliação 180 dias | Grátis | [Microsoft Evaluation Center](https://www.microsoft.com/evalcenter) |
| Windows 10/11 Enterprise — avaliação 90 dias | Grátis | [Microsoft Evaluation Center](https://www.microsoft.com/evalcenter) |
| Windows dev VM (pronta, expira) | Grátis | [Windows dev environment](https://developer.microsoft.com/windows/downloads/virtual-machines/) |
| Security Onion | Grátis | [securityonion.net](https://securityonionsolutions.com/) |
| pfSense CE / OPNsense | Grátis | [opnsense.org](https://opnsense.org/) |

> As avaliações da Microsoft são **legais e renováveis**: quando expira, você recria a VM a partir de um snapshot limpo. É por isso que o passo dos snapshots (abaixo) importa.

### Orçamento de RAM — a conta que decide tudo

Reserve **sempre** 4 GB para o seu sistema hospedeiro. O que sobra é o seu lab:

| VM | RAM mínima | RAM confortável |
|---|---|---|
| Kali Linux (GUI) | 2 GB | 4 GB |
| Kali Linux (sem GUI) | 1 GB | 2 GB |
| Ubuntu Server | 1 GB | 2 GB |
| Windows 10/11 | 4 GB | 8 GB |
| Windows Server + AD | 4 GB | 8 GB |
| Metasploitable / DVWA | 512 MB | 1 GB |
| pfSense / OPNsense | 1 GB | 2 GB |
| Wazuh (all-in-one) | 4 GB | 8 GB |
| Security Onion | 12 GB | 16 GB |

**Com 8 GB de RAM total:** 4 GB host + Kali (2 GB) + Metasploitable (512 MB) + DVWA (512 MB). Suficiente para todo o PortSwigger Academy, TryHackMe e a maior parte dos CTFs.

**Com 16 GB:** 4 GB host + Kali (4 GB) + Windows Server AD (4 GB) + Windows cliente (4 GB). Já dá para lab de Active Directory pequeno.

### Truques que economizam RAM

1. **Nada de interface gráfica em servidor.** Ubuntu Server sem GUI usa ~400 MB; com GUI, 2 GB.
2. **Ligue só o que está usando.** VM desligada não consome RAM. Parece óbvio, e todo mundo deixa 5 ligadas.
3. **Use containers em vez de VMs** quando o alvo for uma aplicação web:
   ```bash
   docker run -d -p 3000:3000 bkimminich/juice-shop
   docker run -d -p 80:80 vulnerables/web-dvwa
   ```
   O Juice Shop em container usa ~200 MB. Em VM, 2 GB.
4. **Disco dinâmico** (não pré-alocado) — cresce só conforme o uso.
5. **Linked clones** no VirtualBox: 5 VMs a partir de uma base ocupam o espaço de ~1,2.

---

## ☁️ Nível 0.5 — Nuvem gratuita (complemento ao nível 0)

Serve para o que precisa ficar **ligado 24/7** e você não quer deixar o notebook aceso: honeypot, servidor de C2 de laboratório, coletor de logs.

| Provedor | O que dá de graça | Pegadinha |
|---|---|---|
| **Oracle Cloud Always Free** | 2 OCPU ARM + 12 GB RAM + 200 GB disco | Limite foi **cortado pela metade em jun/2026** (era 4 OCPU/24 GB). Falta de capacidade na região é comum — pode demorar dias para conseguir criar |
| Google Cloud | e2-micro (1 vCPU, 1 GB) | Muito limitado, serve para pouca coisa |
| AWS Free Tier | 750h/mês de t2.micro por 12 meses | Expira em 1 ano |
| Azure | US$ 200 de crédito por 30 dias + serviços grátis | Crédito curto |

**Regras de sobrevivência na nuvem gratuita:**

- Configure **alerta de orçamento em R$ 0,01** antes de qualquer coisa. Free tier vira conta cara com um clique errado.
- Nunca rode malware em nuvem pública — viola os termos de uso e derruba sua conta.
- Honeypot é permitido pela maioria, mas leia os termos antes.
- Oracle: escolha a região certa na criação — **não dá para mudar depois**, e a capacidade ARM varia por região.

---

## 💻 Nível 1 — Mini PC usado (o melhor custo-benefício)

Quando o notebook começar a engasgar, o caminho mais barato **não é montar um PC** — é comprar um desktop corporativo usado da linha "tiny/micro/mini". São máquinas que custaram ~US$ 900 novas e hoje saem por **US$ 80–180**.

### O que procurar

| Modelo | Geração alvo | Observação |
|---|---|---|
| **Lenovo ThinkCentre M720q / M920q Tiny** | i5-8500T / i7-8700T | Melhor custo-benefício; consome 8–12W em idle |
| **Dell OptiPlex 7060 / 7070 / 7080 Micro** | i5 8ª gen ou superior | Muito comum no mercado usado |
| **HP EliteDesk 800 G4 / G5 Mini** | i5 8ª gen ou superior | Equivalente aos acima |

### Especificação mínima que vale a pena

- **CPU:** Intel 8ª geração ou mais nova (i5 basta). Precisa ter **VT-x e VT-d** — todas as acima têm.
- **RAM:** 16 GB (dois slots SO-DIMM DDR4, aceita até 32 GB)
- **Disco:** SSD de 256 GB no mínimo; tem slot M.2 NVMe
- **Energia:** ~10W em idle — cabe rodar 24/7 sem susto na conta de luz

### O que NÃO comprar

- ❌ **Servidor de rack antigo** (Dell R710 e similares). Parece tentador pelo preço, mas faz barulho de aspirador, consome 200W+ e a conta de luz supera o preço do mini PC em poucos meses.
- ❌ **Raspberry Pi como host principal.** É ARM — muita imagem de lab (Windows, Metasploitable, boa parte das VMs de segurança) simplesmente não roda. Serve como alvo ou honeypot, não como hypervisor.
- ❌ **Máquina com menos de 8 GB e sem slot para expandir.**
- ❌ **CPU anterior à 6ª geração Intel** — falta suporte de virtualização moderno.

### Onde procurar no Brasil

Busque pelos nomes exatos dos modelos acima em Mercado Livre, OLX e lojas de recondicionados corporativos. Leilões e desmobilização de empresas costumam ter os melhores preços. **Confira o preço atual antes de decidir** — o mercado usado varia muito, e o valor de referência em dólar acima é do mercado americano.

Ao comprar, confirme: geração da CPU, quantidade de RAM, se acompanha SSD e se tem fonte original.

### Qual hypervisor instalar

| Opção | Quando usar |
|---|---|
| **Proxmox VE** (grátis) | Recomendado. Gerencia pelo navegador, tem snapshot, clone e container LXC nativo |
| VirtualBox sobre Ubuntu | Se você já conhece e quer usar a máquina para outras coisas |
| ESXi | Evite — licenciamento gratuito mudou e ficou restritivo |

---

## 🔧 Nível 2 — Upgrades por ordem de impacto

1. **RAM 16 → 32 GB** (~US$ 30–60 em DDR4 SO-DIMM usada). **É sempre o melhor upgrade.** Destrava GOAD, Security Onion e análise de malware.
2. **SSD NVMe** — se o lab está lento, geralmente é disco, não CPU.
3. **Switch gerenciável barato com VLAN** — só quando for estudar segmentação de rede de verdade.
4. **Segundo mini PC** — para simular ambiente distribuído. Só na fase 3+.

---

## 🌐 Topologias prontas por trilha

### 🔴 Red Team — o lab mínimo (roda em 8 GB)

```
[ Kali Linux 2GB ] ──┐
                     ├── Rede host-only  192.168.56.0/24
[ Metasploitable 512MB ]
[ DVWA/Juice Shop em container ]
```

Cobre: recon, exploração, web hacking, privilege escalation em Linux.

### 🔵 Blue Team — SIEM (precisa de 16 GB)

```
[ Wazuh all-in-one 4GB ] ←── logs ──┬── [ Windows 10 + agente 4GB ]
                                    └── [ Ubuntu + agente 1GB ]
[ Kali 2GB ] ── ataca os alvos para gerar alertas
```

Cobre: coleta de log, regras de detecção, triagem, projeto P5 e P6.

### 🏢 Active Directory (precisa de 16 GB, ideal 32 GB)

```
[ Windows Server DC 4GB ]
[ Windows 10 cliente 4GB ]
[ Kali 4GB ]
```

Para o [GOAD](https://github.com/Orange-Cyberdefense/GOAD) completo, planeje 32 GB. Existe a variante **GOAD-Light**, que roda em 16 GB.

### 🦠 Análise de malware (isolamento obrigatório)

```
[ Windows 10 (snapshot limpo) ] ── rede: NENHUMA ou host-only isolada
[ REMnux ou FlareVM ]
```

**Sem NAT, sem bridge, sem exceção.**

---

## 🔒 Segurança do lab (não pule esta parte)

O maior risco de um home lab não é alguém te invadir — é **você mesmo infectar sua rede de casa**.

### Modos de rede, traduzido

| Modo | O que faz | Use para |
|---|---|---|
| **Host-only** | VMs se enxergam entre si e com o host, sem internet | **Padrão do seu lab.** Alvos vulneráveis, sempre |
| **Internal / Rede interna** | VMs se enxergam só entre si, nem o host acessa | Análise de malware |
| **NAT** | VM acessa internet, ninguém acessa a VM | Kali quando precisar baixar ferramenta |
| **Bridge** | VM entra na sua rede doméstica como um dispositivo real | ⚠️ **Quase nunca.** Nunca com alvo vulnerável ou malware |

### Regras inegociáveis

1. **Metasploitable, DVWA e qualquer alvo vulnerável: só host-only.** São máquinas propositalmente inseguras. Em bridge, qualquer coisa na sua rede as alcança.
2. **Nunca exponha o lab para a internet.** Nada de port forwarding no roteador.
3. **Snapshot antes de qualquer coisa arriscada.** É gratuito e salva horas.
4. **VM de malware nunca volta a ter rede.** Terminou a análise, restaura o snapshot e apaga.
5. **Senha diferente da sua real** em tudo dentro do lab.
6. **Só ataque o que é seu.** No Brasil, acesso não autorizado é crime (Lei 12.737/2012, CP Art. 154-A). Ver [`projetos/00-regras.md`](../projetos/00-regras.md).

### Snapshots — o hábito que mais economiza tempo

```
1. VM instalada e atualizada       → snapshot "base-limpa"
2. Ferramentas instaladas          → snapshot "pronta"
3. Antes de cada experimento       → snapshot "antes-de-X"
4. Quebrou?                        → restaura em 10 segundos
```

Sem snapshot, cada erro custa uma reinstalação. Com snapshot, custa 10 segundos. É a diferença entre experimentar sem medo e ter medo de mexer.

---

## 💸 Custo total, na real

| Cenário | Investimento |
|---|---|
| Notebook que você já tem + software gratuito | **R$ 0** |
| \+ nuvem gratuita (Oracle) | **R$ 0** |
| \+ mini PC usado 16 GB | ~US$ 80–180, uma vez |
| \+ upgrade para 32 GB | ~US$ 30–60, uma vez |
| Energia de um mini PC 24/7 (~10W) | Alguns reais por mês |

**Software: R$ 0 em todos os cenários.** Todo hypervisor, sistema operacional e ferramenta deste guia é gratuito ou tem avaliação legal e renovável.

---

## ❌ Os 7 erros mais comuns

| Erro | Consequência | Correção |
|---|---|---|
| Virtualização desligada na BIOS | VM não liga, você acha que o PC é fraco | Ative VT-x / SVM |
| Alvo vulnerável em modo bridge | Máquina insegura exposta na sua rede | Host-only, sempre |
| Deixar 6 VMs ligadas | Tudo travando | Ligue só o que usa |
| Não tirar snapshot | Reinstalar do zero a cada erro | 3 snapshots por VM |
| Comprar servidor de rack usado | Barulho, 200W, conta de luz | Mini PC tiny |
| Disco pré-alocado | 50 GB some por VM | Disco dinâmico |
| Montar o lab e nunca usar | O erro mais caro de todos | Escolha 1 tarefa antes de montar |

---

## ✅ Próximos passos

Com o lab de pé, você já pode fazer:

- [`projetos/01-fundamentais.md`](../projetos/01-fundamentais.md) — **P1: documentar o home lab** (é o projeto, não o preparo para ele)
- [`projetos/02-blue-team.md`](../projetos/02-blue-team.md) — P5 (SIEM Wazuh) e P6 (lab de detecção)
- [`projetos/03-red-team.md`](../projetos/03-red-team.md) — P13 (relatório de pentest) e P16 (Active Directory)
- [`labs/red-team-ctf.md`](./red-team-ctf.md) e [`labs/blue-team.md`](./blue-team.md) — quando quiser lab pronto sem montar nada

> **Documente enquanto monta**, não depois. Print de cada etapa, decisão de rede anotada, problema que apareceu e como resolveu. Isso é exatamente o conteúdo do P1 — e é o projeto que abre o seu portfólio.

---

## Fontes

- [Used enterprise desktops vs new mini PCs (2026)](https://minipclab.com/blog/used-enterprise-desktops-vs-mini-pc-homelab)
- [Best used mini PCs for a homelab under $200 (2026)](https://budgethomelab.com/articles/used-mini-pc-homelab-under-200/)
- [Oracle corta free tier de 4 OCPU/24GB para 2 OCPU/12GB (jun/2026)](https://www.infoq.com/news/2026/07/oracle-cloud-free-tier-limits/)

---

[⬅️ Voltar ao índice](../README.md)
