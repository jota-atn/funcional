# Snake — decisões de design

Implementação do jogo Snake para terminal em Python, em estilo funcional,
usando o padrão **núcleo funcional, casca imperativa**.

## Como rodar

```sh
cd snake
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Comandos no jogo: `w`/`a`/`s`/`d` (ou as setas) movem a *snake* para
cima/esquerda/baixo/direita, respectivamente; `q` ou Esc encerra o jogo
a qualquer momento. Apertar a direção oposta à atual (ex.: `s` andando
para NORTH) é ignorado, para a *snake* não inverter sobre si mesma
instantaneamente. Ao terminar (por colisão ou por pedido do jogador), o jogo reproduz
automaticamente um "filme" acelerado de toda a partida.

## Arquitetura: núcleo funcional, casca imperativa

```
game/
  result.py     núcleo — monad Result (Ok/Err)
  geometry.py   núcleo — Point, BoardSize, Direction, giros
  commands.py   núcleo — Command, parse_key (String -> Result[Command, str])
  state.py      núcleo — GameState, Status, speed_up
  core.py       núcleo — turn, advance, place_fruit, initial_state
  render.py     núcleo — GameState -> Frame (tupla de strings)
  history.py    núcleo — History, record (lista imutável de estados)
  shell.py       casca — blessed, time, random, o laço do jogo
main.py          casca — ponto de entrada
```

Tudo em `game/*.py`, exceto `shell.py`, é **puro**: nenhuma dessas
funções lê o teclado, escreve na tela, dorme ou chama `random` — tudo
que é não-determinístico (posição da fruta) é recebido como parâmetro
(`choice: Callable[[List[Point]], Point]`), injetado pela casca. Isso é
o que permite, em princípio, testar o núcleo inteiro sem terminal e sem
mocks — o estado é só dado, as transições são só funções.

`shell.py` é a única parte imperativa: abre o terminal com `blessed`,
lê teclas com timeout (o timeout é o próprio "tick" do jogo), e chama o
núcleo para calcular o próximo estado. A casca nunca contém lógica de
jogo — apenas orquestra chamadas ao núcleo e efeitos colaterais
(desenhar, esperar, gerar aleatório).

## Estado do jogo

```python
@dataclass(frozen=True)
class GameState:
    board: BoardSize                 # largura/altura do tabuleiro
    snake: Tuple[Point, ...]         # cabeça é sempre snake[0]; nunca vazia
    direction: Direction             # NORTH | SOUTH | EAST | WEST
    fruit: Point
    score: int
    speed: float                     # segundos por tick; menor = mais rápido
    status: Status                   # RUNNING | GAME_OVER | QUIT | WON
```

Decisões para **evitar estados inválidos por construção**:

- `GameState` é `frozen=True`: nenhuma transição muta o estado anterior,
  toda mudança gera um novo objeto via `dataclasses.replace`.
- `snake` é uma `tuple[Point, ...]` (imutável) em vez de `list`. A
  cabeça é sempre o primeiro elemento — não existe um campo `head`
  separado que pudesse divergir do corpo.
- `direction` é atribuída diretamente a partir da tecla pressionada
  (WASD/setas = direção absoluta), mas `turn` rejeita qualquer comando
  cuja direção seja o `opposite()` da direção atual. Isso torna
  impossível a *snake* inverter sobre si mesma instantaneamente, sem
  precisar de um esquema de giro relativo.
- `status` é um `Enum` fechado (`RUNNING`, `GAME_OVER`, `QUIT`, `WON`):
  qualquer função que recebe um estado sabe exatamente quais status
  existem e o `advance`/`turn` primeiro checam `status is RUNNING`
  antes de fazer qualquer transição — estado terminal é absorvente.
- `Point` e `BoardSize` são `NamedTuple`: comparáveis, hasháveis e
  imutáveis, usados como elementos de `set` para checar colisão e
  células livres em O(1).

## Eventos e transições (núcleo puro)

Todas em `game/core.py`, todas puras (`State -> State`, ou usam `Result`
quando a operação pode falhar):

- `turn(state, command) -> GameState` — aplica direção absoluta; reversão
  instantânea, comandos irrelevantes ou estado não-`RUNNING` retornam o
  estado inalterado.
- `advance(state, choice) -> GameState` — um tick: move a cabeça
  (`wrap` faz o tabuleiro ser toroidal — atravessar uma borda leva à
  borda oposta), decide se a fruta foi comida, cresce ou não o corpo,
  detecta colisão consigo mesma e, se comeu, chama `place_fruit` para
  reposicionar a fruta e aumenta velocidade (`speed_up`).
- `place_fruit(snake, board, choice) -> Result[Point, str]` — calcula
  as células livres e delega a escolha aleatória para `choice`
  (injetada pela casca). Devolve `Err` se o tabuleiro está cheio (o
  jogador venceu preenchendo todo o tabuleiro).
- `initial_state(board, choice) -> GameState` — monta o estado inicial.

Função de alta ordem: `place_fruit` recebe `choice` como parâmetro
(uma função `List[Point] -> Point`), o que permite trocar a estratégia
de escolha sem alterar a lógica de posicionamento; na casca, usa
`random.Random().choice`.

## Tratamento de erros em estilo monádico

`game/result.py` define o monad `Result = Ok[T] | Err[E]`, com `map`,
`bind` e `unwrap_or`. Dois usos concretos:

1. **`parse_key(key_name) -> Result[Command, str]`** (`commands.py`):
   traduzir uma tecla desconhecida em erro, sem lançar exceção. A casca
   consome isso monadicamente:

   ```python
   def apply_key(state: GameState, name: str) -> GameState:
       return (
           parse_key(name)
           .map(lambda command: quit_game(state) if command is Command.QUIT else turn(state, command))
           .unwrap_or(state)
       )
   ```

   Tecla não mapeada -> `Err` -> `unwrap_or(state)` devolve o estado
   inalterado, sem `if/else` explícito sobre "a tecla é válida?".

2. **`place_fruit(...) -> Result[Point, str]`**: tabuleiro cheio vira
   `Err`, e `advance` encadeia com `.map(...).unwrap_or(...)` para
   decidir entre continuar jogando com a nova fruta ou declarar vitória
   (`Status.WON`) sem nunca levantar exceção nem checar `None`.

## Renderização (também pura)

`render.py` traduz `GameState -> Frame` (uma tupla de `str`), incluindo
bordas, símbolos da *snake* (`@`/`o`), fruta (`*`) e barra de status com
pontuação e velocidade. É pura: dado o mesmo estado, sempre produz o
mesmo frame. A casca (`shell.py::draw`) apenas escreve essas strings na
tela via `blessed`. Essa separação é o que permite reusar exatamente a
mesma função de renderização tanto no jogo ao vivo quanto no replay.

## Desafio: o "filme" do jogo

`game/history.py` define `History = Tuple[GameState, ...]` e
`record(history, state) -> History`, uma função pura que apenas anexa
(`(*history, state)`) — o histórico inteiro da partida é outra
estrutura imutável, nunca mutada in-place.

A cada tick, `shell.py::game_loop` grava o estado resultante no
histórico. Quando o jogo termina (por colisão ou por `q`), a casca
chama `play_replay`, que percorre o histórico completo desenhando cada
frame com um atraso fixo bem menor que o da partida original
(`REPLAY_FRAME_DELAY = 0.04s`), reproduzindo a partida do início ao fim
de forma acelerada — reusando a mesma `render_frame` usada durante o
jogo.

## Bibliotecas de terminal

Optei por `blessed` em vez de `curses`: API mais moderna e sem estado
global de janela, `term.inkey(timeout=...)` já resolve leitura de tecla
com timeout (nosso "tick" de jogo) num único método, e
`term.fullscreen()`/`term.cbreak()`/`term.hidden_cursor()` são
gerenciadores de contexto que cuidam de configurar e restaurar o
terminal automaticamente.
