# Segurança automotiva e embarcada

[← Voltar ao índice](../README.md)

---

CAN bus, UDS, ISO/SAE 21434 e ferramental de bancada. Nicho pequeno, bem pago e com barreira de entrada mais baixa do que parece: dá para começar em simulador, sem carro e sem hardware.

<sub>🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva</sub>

<sub>Esta página usa uma quinta coluna, **Nota**, que os arquivos 00–07 não têm. É
deliberado: são áreas de nicho em que o nome do item não diz o que ele é. O
formato segue o de [`labs/`](../labs/), que já usa nota.</sub>

| Curso / material | Fonte | Lang | Tags | Nota |
|---|---|---|---|---|
| ⭐ ⭐ ICSim — simulador de painel e de barramento CAN | [github.com](https://github.com/zombieCraig/ICSim) | 🇺🇸 | 🆓 🧪 | Painel de instrumentos falso que fala CAN por vcan: dá para caçar os IDs de velocidade, portas e setas sem carro e sem hardware, só com Linux e can-utils |
| ⭐ ⭐ Intro to Automotive Cybersecurity | [learn.blockharbor.io](https://learn.blockharbor.io/intro-auto-cybersecurity/) | 🇺🇸 | 🆓 | Curso de 9 módulos em vídeo que cobre arquitetura do veículo, superfícies de ataque, regulação e processo de engenharia — é o ponto de entrada mais completo e sem paywall da área |
| ⭐ ⭐ The Car Hacker's Handbook (livro-curso, CC BY-NC-SA) | [opengarages.org](https://opengarages.org/handbook/) | 🇺🇸 | 🆓 | A referência da área, liberada pelo próprio autor sob Creative Commons: modelagem de ameaça do veículo, CAN, diagnóstico, engenharia reversa de firmware de ECU e bancada barata |
| Barramento CAN entre Arduinos UNO (bancada de ~R$100) | [embarcados.com.br](https://embarcados.com.br/barramento-can-entre-arduinos-uno/) | 🇧🇷 | 🆓 🧪 | Tutorial em português que monta uma rede CAN de verdade com dois Arduinos, MCP2515 e TJA1050, explicando bit dominante/recessivo e arbitragem com código completo |
| Segurança em Redes Veiculares: Inovações e Direções Futuras (minicurso) | [books-sol.sbc.org.br](https://books-sol.sbc.org.br/index.php/sbc/catalog/view/91/401/672) | 🇧🇷 | 🆓 | Capítulo de minicurso em português sobre ameaças, ataques e contramedidas em redes veiculares — o material acadêmico mais sério da área em PT, ainda que centrado em V2X e não em CAN |
| CAN Bus Explained — a simple intro | [csselectronics.com](https://www.csselectronics.com/pages/can-bus-simple-intro-tutorial) | 🇺🇸 | 🆓 | Introdução ao CAN em nível físico e de frame, com as camadas superiores (OBD2, J1939, CAN FD) mapeadas — a base que falta a quem vem de redes IP |
| CaringCaribou — o "nmap do barramento CAN" | [github.com](https://github.com/CaringCaribou/caringcaribou) | 🇺🇸 | 🆓 🧪 | Ferramenta de exploração com módulos de discovery, UDS, XCP e fuzzer, e documentação de uso passo a passo — combina com o ICSim para praticar sem carro |
| ISO/SAE 21434 e CSMS — cláusulas 5 a 15 | [learn.blockharbor.io](https://learn.blockharbor.io/iso-sae-21434-csms/) | 🇺🇸 | 🆓 | Onze vídeos, um por cláusula da ISO/SAE 21434, explicando as 118 provisões da norma — é a forma barata de entender o padrão sem comprar o documento da ISO |
| RAMN — testbed de 4 ECUs, tutoriais de UDS e mini-CTF | [ramn.readthedocs.io](https://ramn.readthedocs.io/en/latest/) | 🇺🇸 | 🆓 🧪 | Documentação aberta de um testbed CAN/CAN-FD de quatro ECUs com capítulos práticos de CAN, ISO-TP e UDS, mini-CTF e write-ups de CTFs automotivos reais |
| Remote Exploitation of an Unaltered Passenger Vehicle (Jeep, 2015) | [illmatics.com](https://illmatics.com/Remote%20Car%20Hacking.pdf) | 🇺🇸 | 🆓 | O estudo de caso que criou a disciplina: cadeia completa de rádio celular até injeção de mensagens CAN em um Jeep Cherokee de série, publicada pelos próprios autores |
| Scapy — camada automotiva (CAN, ISO-TP, UDS, scans de ECU) | [scapy.readthedocs.io](https://scapy.readthedocs.io/en/latest/layers/automotive.html) | 🇺🇸 | 🆓 🧪 | Documentação oficial com código pronto para varrer ECUs, montar pacotes UDS e falar ISO-TP em Python — é o caminho mais curto do teórico ao hands-on |
| UDS Explained — Unified Diagnostic Services (ISO 14229) | [csselectronics.com](https://www.csselectronics.com/pages/uds-protocol-tutorial-unified-diagnostic-services) | 🇺🇸 | 🆓 | O melhor tutorial aberto de UDS: estrutura do frame, serviços, ISO-TP e exemplos de dados reais — leitura obrigatória antes de apontar um scanner para uma ECU |

---

[← Voltar ao índice](../README.md)
