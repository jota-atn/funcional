---
title: Exercícios — Nível 0
sub_title: Mentalidade Funcional
theme:
  name: p1
---

# Exercícios — Nível 0: Mentalidade Funcional

Resolva no papel/cabeça antes de rolar até o gabarito. São perguntas
conceituais e pequenas reescritas, não programas grandes.

<!-- end_slide -->

## 1. Pura ou impura?

Pra cada função abaixo, diga se ela é **pura** ou **impura** e justifique
em uma frase.

**(a)**
```python
def soma(a, b):
    return a + b
```

**(b)**
```python
contador = 0
def proximo_id():
    global contador
    contador += 1
    return contador
```

**(c)**
```python
def primeiro_par(numeros):
    for n in numeros:
        if n % 2 == 0:
            return n
    return None
```

**(d)**
```clojure
(defn media [nums]
  (/ (reduce + nums) (count nums)))
```

**(e)**
```python
def log_e_dobra(n):
    print(f"dobrando {n}")
    return n * 2
```

<!-- end_slide -->

## 2. Transparência referencial

Considere:

```python
def area_quadrado(lado):
    return lado * lado

perimetro = 4 * area_quadrado(5) / area_quadrado(5)
```

Essa expressão pode ser substituída por `4 * 25 / 25` sem mudar o
comportamento do programa? Por quê?

<!-- pause -->

Agora considere:

```python
def area_quadrado_barulhenta(lado):
    print("calculando área...")
    return lado * lado
```

Se você trocar `area_quadrado` por `area_quadrado_barulhenta` na expressão
acima, ela continua referencialmente transparente? O que muda?

<!-- end_slide -->

## 3. Reescreva sem mutação

Reescreva o trecho abaixo (que constrói uma lista de nomes em maiúsculo)
sem usar `.append` nem variável mutada em loop — nem em Python, nem em
Clojure.

```python
nomes = ["ana", "bruno", "carla"]
maiusculos = []
for nome in nomes:
    maiusculos.append(nome.upper())
```

<!-- end_slide -->

## 4. Função que recebe função

Escreva uma função `repete(f, n, x)`, em Python **e** em Clojure, que
aplica `f` a `x`, `n` vezes seguidas (assuma `n >= 0`).

```python
repete(lambda x: x * 2, 3, 1)   # => 8   (1 -> 2 -> 4 -> 8)
```

```clojure
(repete #(* % 2) 3 1) ;; => 8
```

<!-- end_slide -->

## 5. Identifique a mutação escondida

O trecho abaixo *parece* funcional (usa uma função auxiliar), mas ainda
tem um problema de estilo imperativo escondido. Ache o problema.

```python
resultado = []

def processa(n):
    resultado.append(n * 2)

for n in [1, 2, 3]:
    processa(n)
```

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
- (a) **Pura.** Determinística, sem efeito colateral.
- (b) **Impura.** Depende de e altera uma variável externa (`contador`);
  chamar duas vezes com os mesmos argumentos (nenhum, na verdade) produz
  saídas diferentes.
- (c) **Pura.** Não altera nada fora de si, e sempre retorna o mesmo
  resultado para a mesma lista de entrada (mesmo usando um `for`
  internamente — pureza é sobre entrada/saída/efeitos, não sobre a sintaxe
  usada por dentro).
- (d) **Pura.** Mesmo argumento, sempre o mesmo resultado; não altera nada
  externo.
- (e) **Impura.** `print` é um efeito colateral (interage com o mundo fora
  da função), mesmo que o valor de retorno seja determinístico.

<!-- end_slide -->

**2.** Sim, a primeira é substituível: `area_quadrado` é pura, então
`area_quadrado(5)` sempre vale `25`, em qualquer lugar do programa. Com
`area_quadrado_barulhenta`, a substituição por `25` ainda dá o mesmo
*valor numérico* final, mas deixa de ser uma substituição **fiel**, porque
descarta o efeito colateral (o `print`) — o programa deixaria de imprimir
"calculando área..." duas vezes. Ou seja, transparência referencial exige
ausência de efeito colateral, não só determinismo do valor.

<!-- end_slide -->

**3.**
```python
maiusculos = [nome.upper() for nome in nomes]
```
```clojure
(def maiusculos (map clojure.string/upper-case nomes))
```

<!-- end_slide -->

**4.**
```python
def repete(f, n, x):
    for _ in range(n):
        x = f(x)
    return x
```
> Nota: usar um `for` aqui internamente é aceitável neste nível — o ponto é
> que a função em si é pura (não muta nada fora dela) e o "estilo mais
> funcional puro" com recursão é assunto de um nível futuro, ainda não
> coberto por esta trilha. O que importa agora é: `repete` não tem efeito
> colateral e trata `f` como um valor de primeira classe.
```clojure
(defn repete [f n x]
  (if (zero? n)
    x
    (repete f (dec n) (f x))))
```

<!-- end_slide -->

**5.** `processa` é impura: ela não retorna nada de útil e, em vez disso,
faz mutação de uma lista que existe fora dela (`resultado.append`). É o
mesmo problema do item 1(b), só que disfarçado de "função auxiliar". A
versão funcional seria simplesmente `resultado = [n * 2 for n in [1, 2, 3]]`.
