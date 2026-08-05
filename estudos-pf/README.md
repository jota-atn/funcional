---
title: Estudos de Programação Funcional
sub_title: Trilha por Níveis
author: Roteiro de estudos
theme:
  name: p1
---

# Estudos de Programação Funcional — Trilha por Níveis

Este diretório é uma trilha de estudos **cumulativa** de Programação
Funcional, construída em cima do conteúdo dado no curso (material em
`/srv`). A ideia é que você comece do zero e vá subindo de nível conforme
o curso avança — hoje ela cobre mentalidade funcional, a sagrada trindade
(map/filter/reduce), sequências, pipelines e abstração de dados; conforme
novos assuntos forem dados em aula (recursão, mônadas, concorrência,
etc.), novos níveis serão adicionados em cima destes.

<!-- end_slide -->

## Regra do jogo

Os níveis são **sequenciais**: o nível N assume que você domina tudo do
nível N-1. Não pule pra frente só porque um exercício parece fácil —
resolva os exercícios de cada nível, confira no gabarito, e só então avance.

```
nível 0  Mentalidade Funcional (base de tudo)
   │
   ▼
nível 1  map / filter / reduce (a Sagrada Trindade)
   │
   ▼
nível 2  Sequências, comprehensions e generators
   │
   ▼
nível 3  Pipelining / composição em cadeia
   │
   ▼
nível 4  Abstração de Dados sem classes (TADs funcionais)
   │
   ▼
nível 5  Aplicações reais (leitura, sem exercícios)
   │
   ▼
(níveis futuros: recursão, mônadas, concorrência... conforme o curso avança)
```

<!-- end_slide -->

## Estrutura de cada nível

Cada pasta `nivel-N-*` tem:
- `README.md` — o texto explicando o conceito do zero, com exemplos em
  Python e Clojure, e um link claro para o arquivo-fonte em `/srv` onde o
  assunto foi dado em aula.
- `exercicios.md` — problemas de fixação, com o **gabarito no final do
  arquivo** (resolva antes de rolar até lá).

<!-- end_slide -->

## Como progredir

<!-- incremental_lists: true -->

1. Leia o `README.md` do nível.
2. Resolva os exercícios de `exercicios.md` **sem olhar o gabarito**.
3. Confira suas respostas contra o gabarito e entenda qualquer diferença
   (mesmo que sua resposta também esteja correta — pode haver um jeito mais
   idiomático).
4. Só então avance pro próximo nível.

<!-- incremental_lists: false -->

Ao terminar o nível 4, leia o nível 5 — é só texto, mostrando onde essas
mesmas ideias (imutabilidade, map/filter/reduce, pipelines, TADs) aparecem
em sistemas de verdade que você provavelmente já usa.

<!-- end_slide -->

## O que ainda não está aqui

Recursão de cauda/`loop`+`recur`, mônadas/`Result`, tipos algébricos e
concorrência ainda não têm nível próprio — esse conteúdo vem mais adiante
no curso (em `intro-a-recursao.md`, `intro-a-monadas.md`,
`tipos-algebricos.md`). Quando chegar a hora, novos níveis serão
adicionados a esta trilha, continuando de onde o nível 4 parou.
