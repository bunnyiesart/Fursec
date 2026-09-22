// Comportamento das páginas de documento. Nada aqui é obrigatório: sem este
// arquivo a página continua legível, navegável e com o sumário na lateral —
// só perde o estado salvo do checklist e o recolher do sumário no telefone.
(() => {
  'use strict';

  // ── sumário: no telefone começa recolhido ──────────────────────────────
  // O <details> nasce aberto no HTML para funcionar sem script; em tela
  // estreita uma lista de 39 itens empurraria o conteúdo para fora da tela.
  const sumario = document.querySelector('.sumario');
  if (sumario && matchMedia('(max-width: 62rem)').matches) {
    sumario.open = false;
  }

  // ── checklist persistente ──────────────────────────────────────────────
  const itens = [...document.querySelectorAll('.task-list-item')];
  if (!itens.length) return;

  const CHAVE = 'fursec:progresso:' + location.pathname;

  // A chave de cada item é o texto dele, normalizado — não a posição. Assim
  // reordenar a lista não perde marcação, e reescrever um item o trata como
  // item novo, que é o comportamento correto.
  const chaveDe = (li) =>
    li.textContent.trim().toLowerCase()
      .normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 72);

  const ler = () => {
    try {
      return new Set(JSON.parse(localStorage.getItem(CHAVE) || '[]'));
    } catch { return new Set(); }
  };
  const gravar = (set) => {
    try {
      localStorage.setItem(CHAVE, JSON.stringify([...set]));
    } catch { /* modo privado, cota cheia, dados bloqueados: segue sem salvar */ }
  };

  let marcados = ler();

  // ── medidor por seção ──────────────────────────────────────────────────
  // Cada <h2> vira uma seção; os itens que vêm depois dele pertencem a ela.
  const secoes = [];
  let atual = null;
  for (const no of document.querySelectorAll('.md h2, .md .task-list-item')) {
    if (no.tagName === 'H2') {
      atual = { titulo: no, itens: [] };
      secoes.push(atual);
    } else if (atual) {
      atual.itens.push(no);
    }
  }

  const medidores = new Map();
  for (const s of secoes) {
    if (!s.itens.length) continue;
    const el = document.createElement('p');
    el.className = 'medidor';
    el.innerHTML = '<span class="barra"><i></i></span><b></b>';
    s.titulo.insertAdjacentElement('afterend', el);
    medidores.set(s, el);
  }

  const totalGeral = itens.length;

  // O aviso e o botão são criados aqui, não no markdown, por dois motivos: o
  // GitHub sanitiza <button> do markdown cru, e — mais importante — eles só
  // fazem sentido quando há JS para salvar estado. Sem script, a página não
  // promete o que não cumpre.
  const cabeca = document.querySelector('.md h1');
  let resumo = null;
  let limpar = null;
  if (cabeca) {
    const caixa = document.createElement('div');
    caixa.className = 'aviso-local';
    resumo = document.createElement('span');
    resumo.className = 'resumo-progresso';
    limpar = document.createElement('button');
    limpar.type = 'button';
    limpar.className = 'limpar-progresso';
    limpar.textContent = 'Desmarcar tudo';
    caixa.append(resumo, limpar);
    cabeca.insertAdjacentElement('afterend', caixa);
  }

  function pintar() {
    for (const [s, el] of medidores) {
      const feitos = s.itens.filter((li) => marcados.has(chaveDe(li))).length;
      const pct = Math.round((feitos / s.itens.length) * 100);
      el.querySelector('i').style.width = pct + '%';
      el.querySelector('b').textContent = `${feitos}/${s.itens.length}`;
      el.classList.toggle('completo', feitos === s.itens.length);
    }
    for (const li of itens) {
      li.classList.toggle('feito', marcados.has(chaveDe(li)));
    }
    if (resumo) {
      const feitos = itens.filter((li) => marcados.has(chaveDe(li))).length;
      resumo.textContent = feitos
        ? `${feitos} de ${totalGeral} marcados. O estado fica só neste navegador — não sincroniza e some se você limpar os dados do site.`
        : 'Marque o que concluiu. O estado fica só neste navegador — não sincroniza e some se você limpar os dados do site.';
    }
  }

  // O GitHub renderiza os checkbox desabilitados; o build remove o disabled
  // para que eles funcionem aqui.
  for (const li of itens) {
    const cx = li.querySelector('input[type="checkbox"]');
    if (!cx) continue;
    cx.checked = marcados.has(chaveDe(li));
    cx.addEventListener('change', () => {
      const k = chaveDe(li);
      cx.checked ? marcados.add(k) : marcados.delete(k);
      gravar(marcados);
      pintar();
    });
  }

  if (limpar) {
    limpar.addEventListener('click', () => {
      if (!confirm('Desmarcar tudo nesta página? Isto não tem como desfazer.')) return;
      marcados = new Set();
      gravar(marcados);
      for (const li of itens) {
        const cx = li.querySelector('input[type="checkbox"]');
        if (cx) cx.checked = false;
      }
      pintar();
    });
  }

  pintar();
})();
