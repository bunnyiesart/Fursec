# ICS, OT e SCADA — segurança industrial

[← Voltar ao índice](../README.md)

---

Segurança de sistema industrial: PLC, SCADA, Modbus, DNP3, a norma IEC 62443 e o modelo Purdue. Área com demanda alta e pouquíssima gente qualificada, porque exige entender processo físico além de rede.

**Aviso que não é formalidade:** errar num ambiente de OT não derruba um site, para uma linha de produção ou algo pior. Pratique só em simulador ou bancada sua.

<sub>🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva</sub>

<sub>Esta página usa uma quinta coluna, **Nota**, que os arquivos 00–07 não têm. É
deliberado: são áreas de nicho em que o nome do item não diz o que ele é. O
formato segue o de [`labs/`](../labs/), que já usa nota.</sub>

| Curso / material | Fonte | Lang | Tags | Nota |
|---|---|---|---|---|
| ⭐ ⭐ Getting Started with Industrial (ICS/OT) Cyber Security (curso completo no YouTube) | [youtube.com](https://www.youtube.com/playlist?list=PLOSJSv0hbPZAlINIh1HcB0L8AZcSPc80g) | 🇺🇸 | 🆓 | 11 aulas, mais de 20 horas, do modelo Purdue a protocolos e detecção — o melhor ponto de entrada gratuito da área |
| ⭐ ⭐ GRFICSv2 — simulação gráfica de planta química com PLC, HMI e firewall vulneráveis | [github.com](https://github.com/Fortiphyd/GRFICSv2) | 🇺🇸 | 🆓 🧪 | Cinco VMs VirtualBox com processo químico em 3D, OpenPLC vulnerável falando Modbus e pfSense — dá para atacar e ver a planta reagir |
| 4SICS ICS PCAP files — capturas reais de Modbus, DNP3 e S7 | [netresec.com](https://www.netresec.com/?page=PCAP4SICS) | 🇺🇸 | 🆓 🧪 | Tráfego capturado no lab de equipamentos industriais da conferência 4SICS, pronto para abrir no Wireshark e aprender os protocolos de verdade |
| Caldera for OT — emulação de adversário em ambiente industrial | [github.com](https://github.com/mitre/caldera-ot) | 🇺🇸 | 🆓 🧪 | Plugins de Modbus, DNP3, BACnet e Profinet para o Caldera, mapeados no ATT&CK for ICS |
| Conpot — honeypot de ICS/SCADA | [github.com](https://github.com/mushorg/conpot) | 🇺🇸 | 🆓 🧪 | Emula S7comm, Modbus, BACnet e IPMI para ver na prática o que varre uma rede industrial exposta |
| CSET — Cyber Security Evaluation Tool | [github.com](https://github.com/cisagov/cset) | 🇺🇸 | 🆓 🧪 | Ferramenta oficial da CISA para avaliar postura de ICS contra NIST SP 800-82, IEC 62443 e CIS Controls — é a mesma usada no curso 401 |
| ICSNPP — parsers Zeek para protocolos industriais | [github.com](https://github.com/cisagov/ICSNPP) | 🇺🇸 | 🆓 🧪 | Dá ao Zeek visibilidade de Modbus, DNP3, S7comm, BACnet e EtherNet/IP — é como se faz monitoramento passivo em OT |
| Microsoft ICSpector — forense de metadados de PLC | [github.com](https://github.com/microsoft/ics-forensics-tools) | 🇺🇸 | 🆓 🧪 | Extrai e compara lógica e metadados de PLCs Siemens e Rockwell para achar alteração não autorizada de programa |
| MITRE ATT&CK for ICS — matriz de táticas e técnicas | [attack.mitre.org](https://attack.mitre.org/matrices/ics/) | 🇺🇸 | 🆓 | A referência que estrutura qualquer estudo de ameaça em OT: técnicas de impairment de processo, manipulação de PLC e perda de controle |

---

[← Voltar ao índice](../README.md)
