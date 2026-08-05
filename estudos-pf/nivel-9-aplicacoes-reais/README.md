---
title: Nível 9 — Aplicações Reais
sub_title: Onde essas ideias aparecem em sistemas reais
theme:
  name: catppuccin-mocha
---

# Nível 9 — Onde essas ideias aparecem em sistemas reais

**Pré-requisito:** Níveis 0 a 8 completos — este é o **último nível**
desta trilha. Ele não tem exercícios — é só leitura, pra você enxergar
que o conteúdo inteiro que você estudou não é um exercício de sala de
aula isolado: é a base de ferramentas que rodam em produção, em escala
gigante, todo dia.

<!-- end_slide -->

## 1. MapReduce (Google, Hadoop, Apache Spark)

O **Nível 1** inteiro (map/filter/reduce) é literalmente o nome do
paradigma de processamento distribuído criado pelo Google em 2004
(*"MapReduce: Simplified Data Processing on Large Clusters"*) e depois
popularizado pelo Hadoop e pelo Spark.

A ideia: para processar terabytes de dados espalhados em milhares de
máquinas, você descreve o processamento como um `map` (transforma cada
registro, roda em paralelo, uma máquina cuida de um pedaço dos dados) e um
`reduce` (agrega os resultados parciais). Funciona porque `map` sobre uma
função pura não tem dependência entre os elementos — cada máquina processa
seu pedaço sem precisar coordenar com as outras. Se a função não fosse
pura (dependesse de estado compartilhado), paralelizar assim seria
impossível sem travas e coordenação.

<!-- end_slide -->

Uma consulta típica em Spark (Python, via PySpark) é literalmente o
pipeline do **Nível 3**:

```python
resultado = (dados
    .filter(lambda x: x.idade >= 18)
    .map(lambda x: x.salario)
    .reduce(lambda a, b: a + b))
```

<!-- end_slide -->

## 2. Redux / React — gerência de estado com funções puras

Redux (usado com React) organiza todo o estado de uma aplicação web em
torno de **reducers**: funções puras `(estado_atual, acao) -> novo_estado`
que **nunca alteram** o estado recebido — sempre devolvem um objeto novo.
É a mesma regra do TAD Pilha do Nível 4: `f: T -> T`, sem mutação.

```javascript
function reducer(estado, acao) {
  switch (acao.tipo) {
    case "INCREMENTA":
      return { ...estado, contador: estado.contador + 1 }; // objeto NOVO
    default:
      return estado;
  }
}
```

<!-- end_slide -->

Por que isso importa na prática? Porque o React usa **transparência
referencial** pra decidir se precisa re-renderizar um componente: se o
objeto de estado é o mesmo objeto de antes (mesma referência), ele sabe
que nada mudou e pula o trabalho. Se você mutasse o estado em vez de criar
um novo, o React não teria como perceber a mudança de forma barata.

<!-- end_slide -->

## 3. Git — estrutura de dados persistente

Cada commit no Git é **imutável**: uma vez criado, seu conteúdo e seu hash
nunca mudam. "Desfazer" um commit não apaga o antigo — cria um novo
apontando pra ele. Um branch é só um ponteiro (nome) apontando pro commit
mais recente de uma linha de histórico.

<!-- pause -->

Isso é exatamente o padrão de **estrutura de dados persistente** que o
TAD Pilha do Nível 4 implementa em miniatura: o "estado anterior"
(`p2_backup`) continua válido e acessível depois que você cria o "estado
novo" (`p2` com mais um elemento) — nada foi destruído.

<!-- end_slide -->

## 4. SQL, pandas — pipelines declarativos

Uma consulta SQL não diz *como* buscar os dados (não é um algoritmo passo
a passo) — diz *o quê* você quer, em termos de filtros, transformações e
agregações. É a mesma mentalidade do **Nível 0**:

```sql
SELECT categoria, SUM(valor)
FROM vendas
WHERE valor > 100
GROUP BY categoria
```

<!-- end_slide -->

O equivalente em `pandas` (Python) é literalmente um pipeline no estilo do
**Nível 3**:

```python
(vendas
    .query("valor > 100")
    .groupby("categoria")["valor"]
    .sum())
```

Cada `.método()` encadeado é um passo do pipeline — a mesma ideia do `->>`
do Clojure, só que com sintaxe de "método" em vez de macro.

<!-- end_slide -->

## 5. Pipes do Unix — composição na linha de comando

```bash
cat log.txt | grep "ERROR" | wc -l
```

Cada comando é uma função pura sobre um fluxo de texto: recebe entrada,
produz saída, sem efeito colateral sobre o comando anterior ou seguinte.
`|` é, na prática, uma composição de funções — igual ao `->>` do Clojure ou
aos generators encadeados do **Nível 3**, só que operando sobre processos
do sistema operacional em vez de sequências em memória.

<!-- end_slide -->

## 6. Sistemas de eventos / streaming (Kafka Streams, RxJS)

Sistemas que processam fluxos contínuos de eventos (cliques em um site,
transações bancárias, sensores de IoT) tratam o fluxo como uma **sequência
preguiçosa** (Nível 2) que nunca termina, e descrevem o processamento como
um pipeline de `map`/`filter`/`reduce` sobre esse fluxo:

```javascript
// RxJS (JavaScript) — observar cliques, filtrar e transformar
cliques$
  .pipe(
    filter(evento => evento.botao === "comprar"),
    map(evento => evento.produtoId)
  )
  .subscribe(id => registrarCompra(id));
```

<!-- pause -->

A mesma ideia do generator `contagem_regressiva` do Nível 2 — só que a
"fonte" é um fluxo de eventos do mundo real em vez de um `while True`
programado.

<!-- end_slide -->

## 7. Event Sourcing — abstração de dados sem mutação, em bancos

Sistemas bancários e de auditoria sérios frequentemente usam **event
sourcing**: em vez de guardar "o saldo atual" e sobrescrevê-lo a cada
transação (mutação), guardam a **sequência imutável de eventos**
("depositou 100", "sacou 30", ...) e calculam o saldo atual como um
`reduce` sobre essa sequência.

<!-- pause -->

Isso dá auditoria completa de graça (nada foi sobrescrito, o histórico
inteiro sempre existe) — é o TAD do **Nível 4** aplicado a dinheiro: cada
operação é `f: Historico -> Historico`, e o "saldo" nunca é armazenado
diretamente, é derivado.

<!-- end_slide -->

## 8. Recursão em compiladores, parsers e árvores de arquivos

Qualquer ferramenta que processa código-fonte (compiladores,
interpretadores, formatadores como o `black` de Python) representa o
programa como uma **árvore** (a *AST* — árvore de sintaxe abstrata) e
percorre essa árvore recursivamente: cada nó pode conter outros nós do
mesmo tipo, então a função que processa um nó chama a si mesma para
processar os filhos — exatamente a estrutura do **Nível 5**.

```python
def avalia(no):
    if no.tipo == "numero":
        return no.valor
    if no.tipo == "soma":
        return avalia(no.esquerda) + avalia(no.direita)  # chamada recursiva
```

O mesmo vale para percorrer diretórios (`os.walk`, recursivamente, uma
pasta pode conter outras pastas) e para navegar HTML/JSON aninhado.

<!-- end_slide -->

## 9. Tipos algébricos em linguagens de produção

O que o **Nível 6** chamou de "tipo soma" tem nome e sintaxe própria em
várias linguagens usadas em produção hoje. Em Rust, um `enum` é
literalmente um tipo soma, e o compilador **obriga** você a tratar
todos os casos:

```rust
enum Forma {
    Circulo(f64),           // um F64 (raio)
    Retangulo(f64, f64),    // dois f64 (lados)
}

fn area(f: Forma) -> f64 {
    match f {
        Forma::Circulo(r) => std::f64::consts::PI * r * r,
        Forma::Retangulo(a, b) => a * b,
    }   // esquecer um caso é ERRO DE COMPILAÇÃO, não bug em produção
}
```

TypeScript tem o mesmo padrão com *union types* (`type Forma = Circulo
| Retangulo`) e *discriminated unions* — o `match..case` do Python que
vimos no Nível 6 é a versão mais recente dessa mesma ideia chegando a
uma linguagem mainstream.

<!-- end_slide -->

## 10. `Result`/`Option` em produção: Rust

Rust vai além de recomendação: a linguagem **não tem exceções para
erros recuperáveis**. Toda função que pode falhar é obrigada, pelo
sistema de tipos, a devolver `Result<T, E>` — exatamente o padrão do
**Nível 7**, só que imposto pelo compilador em vez de por convenção:

```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        return Err("divisão por zero".to_string());
    }
    Ok(a / b)
}

fn processa(a: f64, b: f64) -> Result<f64, String> {
    divide(a, b).map(|r| r * 2.0)   // o mesmo .map() do Nível 7
}
```

O operador `?` de Rust (`divide(a, b)?`) é açúcar sintático para "se
`Err`, retorne o erro imediatamente; se `Ok`, desempacote e continue" —
o mesmo `.and_then()` encadeado, só que embutido na sintaxe da
linguagem.

<!-- end_slide -->

## 11. Cálculo lambda por trás das linguagens do dia a dia

O **Nível 8** não é curiosidade histórica isolada — é o modelo que
diversas linguagens usam de fato, direta ou indiretamente:

- **Arrow functions de JavaScript** (`a => b => a`) são, literalmente,
  a notação do cálculo lambda com `λ` trocado por `=>`;
- **currying nativo** em Haskell, OCaml e F# (toda função de "vários
  argumentos" é, por trás, uma cadeia de funções de um argumento só,
  igual vimos com `f a b = (f a) b`);
- **closures** — uma função que "lembra" variáveis do escopo onde foi
  criada — são a versão prática de abstrações como `λa. (λb. a)` do
  Nível 8, que capturam `a` dentro da função interna;
- os algoritmos de **inferência de tipos** de TypeScript, Rust e OCaml
  (Hindley-Milner e variantes) são construídos formalmente em cima do
  cálculo lambda tipado — a matemática que valida "esse tipo bate com
  aquele" antes mesmo do programa rodar vem diretamente daqui.

<!-- end_slide -->

## O fio condutor de toda a trilha

Em todo exemplo acima, a razão de ser dessas escolhas é sempre a mesma:
**funções puras + imutabilidade permitem raciocinar sobre uma parte do
sistema sem precisar entender o sistema inteiro**, e habilitam
paralelismo, cache, undo/histórico, tratamento de erro sem exceções e
testes automáticos de um jeito que código com mutação espalhada não
permite. Da mentalidade funcional do Nível 0 até o modelo teórico
mínimo do cálculo lambda no Nível 8, é essa mesma ideia — funções como
as únicas peças de que você precisa — que sustenta tudo o que você
estudou nesta trilha.
