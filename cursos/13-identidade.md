# Identidade e acesso

[← Voltar ao índice](../README.md)

---

Active Directory, Kerberos, Entra ID, SAML, OAuth e OIDC. É por onde a maior parte dos incidentes corporativos reais passa, e é a área que mais compensa estudar tanto do lado ofensivo quanto do defensivo.

<sub>🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva</sub>

<sub>Esta página usa uma quinta coluna, **Nota**, que os arquivos 00–07 não têm. É
deliberado: são áreas de nicho em que o nome do item não diz o que ele é. O
formato segue o de [`labs/`](../labs/), que já usa nota.</sub>

| Curso / material | Fonte | Lang | Tags | Nota |
|---|---|---|---|---|
| ⭐ Executar tarefas básicas de identidade e acesso (Microsoft Entra ID) | [learn.microsoft.com](https://learn.microsoft.com/pt-br/training/paths/perform-basic-identity-access-tasks/) | 🇧🇷🇺🇸 | 🆓 🎓 🧪 | Caminho de 5 módulos que cobre usuários, grupos, licenças, funções, MFA, SSPR e acesso condicional, e termina em um módulo de laboratórios interativos no próprio Entra |
| ⭐ OAuth 2.0 and OpenID Connect (in plain English) | [youtube.com](https://www.youtube.com/watch?v=996OiexHze0) | 🇺🇸 | 🆓 | Uma hora que resolve a confusão entre OAuth e OIDC — grants, flows, escopos e tokens — e é o pré-requisito mental para entender SSO em qualquer produto |
| ⭐ The Hacker Recipes — Kerberos (ataque e defesa em AD) | [thehacker.recipes](https://www.thehacker.recipes/ad/movement/kerberos/) | 🇺🇸 | 🆓 | Catálogo técnico das técnicas de Kerberos que aparecem em incidente real: Kerberoasting, AS-REP roasting, golden e silver ticket, delegações (KUD, KCD, RBCD), S4U e relay |
| Curso Grátis de Windows Server e Active Directory — 414 videoaulas | [youtube.com](https://www.youtube.com/playlist?list=PLqjSTsK75fSeuSEVCmiP5MkdcNBFRujge) | 🇧🇷 | 🆓 | O material PT-BR mais completo que existe de administração de AD (domínio, florestas, OUs, GPO, DNS, usuários e grupos) — é a base que falta antes de estudar ataque a identidade |
| Práticas recomendadas para proteger o Active Directory | [learn.microsoft.com](https://learn.microsoft.com/pt-br/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory) | 🇧🇷 | 🆓 | A referência oficial de hardening de AD DS em português: superfície de ataque de contas privilegiadas, modelo de camadas administrativas, monitoramento e redução de privilégio |
| Designing an Authentication System: a Dialogue in Four Scenes (Kerberos) | [web.mit.edu](https://web.mit.edu/kerberos/dialogue.html) | 🇺🇸 | 🆓 | Deriva o Kerberos do zero em forma de diálogo, cena a cena — depois dele TGT, ticket de serviço e replay deixam de ser decoreba |
| Entra ID Attack & Defense Playbook | [github.com](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) | 🇺🇸 | 🆓 | Cada capítulo pega um ataque real de Entra ID — password spray, consent grant, replay de PRT, AiTM, conta do Entra Connect Sync — e mostra detecção, mitigação e o mapeamento MITRE ATT&CK |
| Introdução ao JSON Web Token (JWT) | [jwt.io](https://jwt.io/introduction) | 🇺🇸 | 🆓 | Explica header, payload e assinatura, HMAC vs. par de chaves e o uso do Bearer token — e o debugger ao lado deixa inspecionar um token de verdade |
| Mimikatz — guia de referência completo | [adsecurity.org](https://adsecurity.org/?page_id=1821) | 🇺🇸 | 🆓 | Referência de comandos do Mimikatz lado a lado com detecção e defesa, ligada a golden/silver/trust tickets e ao dump de credenciais do AD |
| OAuth 2.0 Simplified (edição web completa) | [oauth.com](https://www.oauth.com/) | 🇺🇸 | 🆓 | O livro inteiro de OAuth 2.0 lido no navegador, do fluxo de authorization code e PKCE a escopos, redirect URLs, introspecção e OIDC |
| Passkey Central — guias de adoção de passkeys | [passkeycentral.org](https://www.passkeycentral.org/) | 🇺🇸 | 🆓 | O lado defensivo moderno: como projetar, implantar e medir autenticação resistente a phishing, direto de quem escreve o padrão FIDO2/WebAuthn |
| SAML V2.0 Technical Overview | [docs.oasis-open.org](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) | 🇺🇸 | 🆓 | O documento que explica SAML de verdade: asserções, bindings, Web Browser SSO iniciado por SP e por IdP, single logout e federação de identificadores |
| SC-300 — laboratórios oficiais do curso (28 labs de Entra ID) | [microsoftlearning.github.io](https://microsoftlearning.github.io/SC-300-Identity-and-Access-Administrator/) | 🇺🇸 | 🆓 🧪 | As instruções de laboratório do curso oficial SC-300, de gestão de usuários e identidade híbrida a acesso condicional, PIM, revisões de acesso e governança — exige um tenant de avaliação para executar |

---

[← Voltar ao índice](../README.md)
