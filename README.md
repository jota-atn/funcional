# funcional

Repositório dedicado aos roteiros de estudo e práticas de laboratório da disciplina de Programação Funcional.

Cada `roteiro-XX/` contém um ou mais exercícios (`qNN.nome/`), com um `README.md`
descrevendo o enunciado e os arquivos de solução da questão.

## Roteiros

| Roteiro | Tema | Linguagem(ns) |
|---|---|---|
| [roteiro-01](roteiro-01) | Introdução a Clojure | Clojure, Python |
| [roteiro-02](roteiro-02) | Processamento de listas (map/filter/reduce) | Clojure |
| [roteiro-03](roteiro-03) | Pedidos e eventos | Clojure |
| [roteiro-04](roteiro-04) | Sequências preguiçosas (lazy sequences) | Python |
| [roteiro-05](roteiro-05) | Especificação e implementação de TADs (pilhas e filas) | Python |
| [roteiro-06](roteiro-06) | Recursão e tail-call | Clojure |
| [roteiro-07](roteiro-07) | Pipelines com o tipo `Result` | Python |
| [roteiro-08](roteiro-08) | `Optional`/`Stream`/`Result` monádicos | Java, Rust |
| [roteiro-09](roteiro-09) | Projeto: jogo Snake em estilo funcional | Python |

## Como rodar

### Clojure

Requer o [Clojure CLI](https://clojure.org/guides/install_clojure) instalado.

```sh
clojure caminho/para/o/arquivo.clj
```

### Python

Cada exercício em Python é independente. Quando houver `requirements.txt`
(ex: `roteiro-09/snake`), crie um ambiente virtual antes de instalar as
dependências:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Os testes (quando existentes) usam `pytest`:

```sh
pytest
```

### Java

```sh
javac *.java
java NomeDaClasse
```

### Rust

```sh
cargo test
```
