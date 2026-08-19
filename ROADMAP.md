# 🗺️ Roadmap — Fursec

> O **quando**. Fases medidas em horas de estudo, não em datas.
> Catálogo completo do que existe: [`cursos/`](./cursos/) · Certificações: [`docs/certificacoes.md`](./docs/certificacoes.md)

---

## How to read this

Every phase has an **hour budget**. Convert to calendar time with your own pace:

| Your pace | Phase 0+1 (~180h) | Through Phase 3 (~450h) | Full roadmap (~650h) |
|---|---|---|---|
| 5 h/week | ~9 months | ~21 months | ~30 months |
| 10 h/week | ~4.5 months | ~11 months | ~15 months |
| 20 h/week | ~2 months | ~5.5 months | ~8 months |

Two parallel columns run through the whole thing:

- 🟢 **FREE LANE** — costs nothing, ever. Everyone does this lane.
- 💳 **PAID LANE** — optional exam vouchers. Never pay for *learning*; pay only for the *exam* that proves it. Tips in [Paid Lane](#-paid-lane--when-to-actually-spend-money).

**Rule of thumb:** don't buy an exam until you can already pass a free practice test at 85%.

---

## Phase 0 — Foundations (~70h)

You cannot secure what you don't understand. Skip this only if you already admin Linux and can explain a TCP handshake.

| # | What | Where | Hours | Free cert? |
|---|---|---|---|---|
| 0.1 | Networking basics (OSI, TCP/IP, DNS, DHCP, routing) | [Cisco Networking Basics](https://www.netacad.com/courses/networking-basics) | 20 | ✅ Badge |
| 0.2 | Intro to Cybersecurity | [Cisco Intro to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity) | 6 | ✅ Badge |
| 0.3 | Linux command line | [TryHackMe Pre-Security path](https://tryhackme.com/path/outline/presecurity) (free rooms) + [Linux Journey](https://linuxjourney.com/) | 20 | ⚪ |
| 0.4 | Windows internals + AD basics | [Microsoft Learn — Windows Server fundamentals](https://learn.microsoft.com/training/) | 12 | ⚪ |
| 0.5 | Threat landscape awareness | [Fortinet NSE 1 + 2 + 3](https://training.fortinet.com/) | 6 | ✅ 3 badges |
| 0.6 | Build a home lab | VirtualBox/Proxmox + Kali + Ubuntu + Windows eval VMs | 6 | ⚪ |

**Exit test:** you can spin up a VM, read `ip a`, capture traffic in Wireshark, and explain what a firewall rule does.

---

## Phase 1 — Security Core (~110h)

Everything below is shared by all four tracks. Do not fork yet.

| # | What | Where | Hours |
|---|---|---|---|
| 1.1 | Security fundamentals (CIA, AAA, controls, crypto basics) | [Professor Messer Security+ course](https://www.professormesser.com/) — 100% free video | 35 |
| 1.2 | Cybersecurity analyst foundations | [IBM SkillsBuild — Cybersecurity Fundamentals](https://skillsbuild.org/) | 15 |
| 1.3 | Google Cybersecurity Certificate (audit / financial aid) | [Coursera](https://www.coursera.org/professional-certificates/google-cybersecurity) — audit free, or apply Financial Aid for the cert | 25 |
| 1.4 | Microsoft security/compliance/identity fundamentals | [SC-900 learning path on Microsoft Learn](https://learn.microsoft.com/training/) | 12 |
| 1.5 | MITRE ATT&CK literacy | [MITRE ATT&CK official training](https://attack.mitre.org/resources/training/) | 10 |
| 1.6 | Scripting: Python + Bash for security | [Automate the Boring Stuff](https://automatetheboringstuff.com/) | 13 |

**Exit test:** you can score >80% on free Security+ practice questions and write a Python script that parses a log file.

💳 *First sensible paid moment is here — see [When to buy Security+](#-paid-lane--when-to-actually-spend-money).*

---

## Phase 2 — The Fork: Hands-On per Track (~120h each)

Pick **one** primary track now. You said all four interest you — that's fine, but do them **sequentially**, not in parallel. Order I'd recommend: **Blue Team → Cloud → Red Team → GRC** (blue team hires fastest, cloud pays most, red team is the most competitive entry, GRC rewards experience you don't have yet).

### 🔵 2A — Blue Team / SOC Analyst (~120h)

| What | Where | Hours | Free? |
|---|---|---|---|
| SOC Level 1 path | [TryHackMe SOC Level 1](https://tryhackme.com/path/outline/soclevel1) | 45 | Partly free, ~$14/mo for full |
| Splunk fundamentals + BOTS datasets | [Splunk Free Training](https://www.splunk.com/en_us/training/free-courses/overview.html) + [BOTS](https://bots.splunk.com/) | 20 | ✅ Free |
| Alert triage in a real SOC UI | [LetsDefend free tier](https://letsdefend.io/) | 20 | ✅ Free tier |
| DFIR / blue team challenges | [CyberDefenders](https://cyberdefenders.org/) — generous free labs | 20 | ✅ Free tier |
| Investigation depth | [Blue Team Labs Online](https://blueteamlabs.online/) free challenges | 15 | ✅ Partly |

### 🔴 2B — Red Team / Pentest (~120h)

| What | Where | Hours | Free? |
|---|---|---|---|
| Web vulns — the gold standard | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | 45 | ✅ 100% free |
| Jr Penetration Tester path | [TryHackMe](https://tryhackme.com/path/outline/jrpenetrationtester) | 35 | Partly free |
| Linux privesc wargames | [OverTheWire Bandit → Natas](https://overthewire.org/wargames/) | 15 | ✅ Free |
| Practical ethical hacking | [TCM Security YouTube](https://www.youtube.com/@TCMSecurityAcademy) full courses | 15 | ✅ Free |
| CTF muscle | [picoCTF](https://picoctf.org/) | 10 | ✅ Free |

### ☁️ 2C — Cloud Security (~120h)

| What | Where | Hours | Free? |
|---|---|---|---|
| Azure security ops (SC-200 path) | [Microsoft Learn](https://learn.microsoft.com/training/) | 35 | ✅ Free |
| AWS security fundamentals + labs | [AWS Skill Builder](https://skillbuilder.aws/) free tier + Builder Labs | 30 | ✅ Free tier |
| GCP security badges | [Google Cloud Skills Boost](https://www.cloudskillsboost.google/) free courses | 25 | ✅ Free tier |
| Cloud attack/defense practice | [flaws.cloud](http://flaws.cloud/) + [flaws2.cloud](http://flaws2.cloud/) + [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | 20 | ✅ Free |
| IaC + container security | [Kubernetes Goat](https://madhuakula.com/kubernetes-goat/) | 10 | ✅ Free |

### 📋 2D — GRC / Compliance (~90h)

| What | Where | Hours | Free? |
|---|---|---|---|
| NIST Cybersecurity Framework 2.0 | [NIST CSF official resources](https://www.nist.gov/cyberframework) | 20 | ✅ Free |
| NIST RMF + SP 800-53 | [NIST RMF training](https://csrc.nist.gov/projects/risk-management/rmf-courses) | 20 | ✅ Free |
| Federal/critical-infra courses | [CISA free training](https://www.cisa.gov/resources-tools/training) + [FEMA IS courses](https://training.fema.gov/is/) | 20 | ✅ Free + certs |
| ISO 27001 structure | [ISO 27001 overview material](https://www.iso.org/standard/27001) + free vendor webinars | 15 | ✅ Free |
| Risk & audit practice | Build a real risk register + control matrix for a fake company | 15 | ✅ Free |

---

## Phase 3 — Depth & Proof (~150h)

Now you specialize *and* you make it visible. Split roughly 60/40 between learning and producing artifacts.

| # | What | Hours |
|---|---|---|
| 3.1 | Advanced path in your chosen track (HTB Academy free modules, Antisyphon pay-what-you-can courses, OpenSecurityTraining2) | 60 |
| 3.2 | **Home lab project** — build a detection lab (Security Onion / Wazuh / ELK), attack it, detect yourself | 40 |
| 3.3 | **Write it up** — 6–10 blog posts or GitHub writeups documenting labs, CTFs, detections you built | 30 |
| 3.4 | Second track from Phase 2 (breadth) | 20 |

**This phase is what actually gets you hired.** Certificates get past HR; the lab writeups get you past the technical interview.

---

## Phase 4 — Job-Ready (~100h, ongoing)

| # | What | Hours |
|---|---|---|
| 4.1 | Resume + LinkedIn rebuilt around projects, not courses | 10 |
| 4.2 | Interview prep — practice explaining your labs out loud | 20 |
| 4.3 | Contribute: open-source detection rules (Sigma), CTF writeups, bug bounty on [HackerOne](https://hackerone.com/) free programs | 40 |
| 4.4 | Continuous: [SANS free webcasts](https://www.sans.org/webcasts/), threat intel newsletters, Simply Cyber daily briefs | 30+ |

---


---

## Ordem sequencial condensada

Se você quiser apenas **uma lista sequencial** sem pensar muito:

1. Cisco *Introdução à Cibersegurança* 🇧🇷 → 2. Cisco *Conceitos Básicos de Redes* 🇧🇷 → 3. Fundação Bradesco *Segurança em TI* 🇧🇷 → 4. CC50/CS50 → 5. TCM *Linux 100* → 6. Fortinet FCF+FCA → 7. Professor Messer Security+ 🇺🇸 → 8. Google Cybersecurity Certificate → 9. **ESCOLHA A TRILHA** → 10a. Blue: THM SOC L1 + Splunk + LetsDefend + CyberDefenders · 10b. Red: PortSwigger + Solyd Intro + THM Jr Pentester + picoCTF · 10c. Cloud: SC-200 + AWS Skill Builder + flaws.cloud · 10d. GRC: LGPD EV.gov + CIS Controls + NIST CSF → 11. Home lab + writeups → 12. Certificação paga (ver roadmap).

> **Meta-conselho:** você não vai terminar tudo aqui — e nem deve. Este catálogo é um **menu**, não uma lista de tarefas. Escolha 1 curso por vez, termine, documente, e só então pegue o próximo.

---

## Próximos passos

- Projetos para provar cada fase → [`projetos/`](./projetos/)
- Como estudar de forma eficiente → [`docs/metodo-de-estudo.md`](./docs/metodo-de-estudo.md)
- Acompanhar progresso → [`progresso/checklist.md`](./progresso/checklist.md)
