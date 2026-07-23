---
options:
    auto_split_overflowing_slides: true
title: Introdução a Lisp e a Clojure a partir de Python
author: Dalton Serey
date: abr/2026
---

# Roteiro 01

## Introdução à sintaxe e semântica Lisp e Clojure

No roteiro, assumo que você está trabalhando em um ambiente com Clojure
instalado.

<!-- end_slide -->
# Como iniciar um REPL Clojure?

```shell
$ clj
Clojure 1.12.1
user=>
```

Este é o REPL da distribuição oficial de Clojure. Como roda sobre
a JVM, costuma ser um pouco lento pra iniciar.

<!-- end_slide -->
# Uma alternativa útil de REPL e Clojure

```shell
$ bb
Babashka v1.12.206 REPL.
Use :repl/quit or :repl/exit to quit the REPL.
Clojure rocks, Bash reaches.

user=>
```

Esta é uma distribuição que gosto muito, por dois motivos: 1) não
roda sobre a JVM, logo é bem rápida; e 2) como é feita para
escrever scripts em Linux, já tem alguns elementos pré-definidos
que facilitam a escrita de scrips simples. Às vezes, contudo, é
preciso usar a versão oficial.

Fique à vontade pra usar a que preferir.

<!-- end_slide -->
# Vale a pena usar o rlwrap com bb

```shell
$ alias bb="rlwrap bb"
$ bb
Babashka v1.12.206 REPL.
Use :repl/quit or :repl/exit to quit the REPL.
Clojure rocks, Bash reaches.

user=>
```

Infelizmente, o `bb` não tem edição de linha implementada (tente
corrigir erros de digitação pra ver). Pra facilitar, use o `bb`
com o wrapper de readline como indicado acima. Pode valer a pena
fazer o alias indicado e colocá-lo no seu `.bashrc`, pra não ter
que ficar digitando o tempo todo.

<!-- end_slide -->
# Sintaxe Clojure / Lisp: expressões simples

Em Python
```Python
1 + 2
3 * 5
```

Em Lisp / Clojure
```Clojure
(+ 1 2)
(* 3 5)
```

É comum lermos `(+ 1 2)` como "_a soma de 1 e 2_". O
primeiro elemento da expressão é sempre a operação que
será aplicada aos demais elementos que são os operandos ou
argumentos.

<!-- end_slide -->
# Sintaxe Clojure / Lisp: expressões compostas

Em Python
```Python
2 * 3 + 4       # 10
2 + 3 * 4       # 14
```

Em Lisp / Clojure
```Clojure
(+ 2 (* 3 4))   ;; 10
(+ (* 2 3) 4)   ;; 14
```

Em Lisp/Clojure, não há precedência de operadores. A ordem das
operações é completamente definida pelo código escrito pelo
programador. Compare as expressões acima.


<!-- end_slide -->
# Sintaxe Clojure / Lisp: definição de variáveis

Em Python
```Python
x = 2 * 3 + 4           # x -> 10
y = 2 + 3 * 4           # y -> 14
```

Em Lisp / Clojure
```Clojure
(def x (+ 2 (* 3 4)))   ;; x -> 10
(def y (+ (* 2 3) 4))   ;; y -> 14
```

Em Python variáveis são _nomes_ ligados (_bound_) a _valores_. Em
Lisp/Clojure é semelhante: variáveis são _bindings_ (ligações)
entre _símbolos_ e _valores_.


<!-- end_slide -->
# Sintaxe Clojure / Lisp: uso de variáveis

Em Python
```Python
x = 2 * 3 + 4           # x -> 10
y = 2 + 3 * 4           # y -> 14
z = (x * y) + 1
```

Em Lisp / Clojure
```Clojure
(def x (+ 2 (* 3 4)))   ;; x -> 10
(def y (+ (* 2 3) 4))   ;; y -> 14
(def z (+ (* x y) 1)    ;; z -> 141
```


<!-- end_slide -->
# Sintaxe Clojure / Lisp: definição de funções

Em Python
```Python
def media(a, b):
    soma = a + b
    media = soma / 2.0
    return media
```

Em Lisp / Clojure
```Clojure
(defn media [a b]
  (let [soma (+ a b)
        media (/ soma 2.0)] 
    media))
```


<!-- end_slide -->
# Sintaxe Clojure / Lisp: uso de funções

Em Python
```Python
a = 10
b = 5
med = media(a, b)
```

Em Lisp / Clojure
```Clojure
(def a 10)
(def b 5)
(def med (media a b))
```


<!-- end_slide -->
# Sintaxe Clojure / Lisp: `let` e variáveis locais

```Clojure
(defn media [a b]
  (let [soma (+ a b)
        media (/ soma 2.0)] 
    media))
```

O programa acima define duas **variáveis locais**, chamadas `soma` e
`media`. E o valor retornado é `media`. Observe bem a sintaxe.
Em particular, o uso dos colchetes ao redor dos _bindings_ no
início do `let` e a expressão `media` ao final do `let` que é o
valor a ser retornado pela função (a expressão no fim do `let` é
que pode usar os valores definidos no `let`).

Essa é a indentação padrão em Clojure.

<!-- end_slide -->
# Sintaxe Clojure / Lisp: condicionais

Em Python
```Python
if num < 0:
    tipo = "negativo"
elif num == 0:
    tipo = "zero"
else:
    tipo = "positivo"
```

Em Lisp / Clojure
```Clojure
(def tipo (cond
            (< num 0)    "negativo"
            (= num 0)    "zero"
            :else        "positivo"))
```


<!-- end_slide -->
# Sintaxe Clojure / Lisp: condicionais 2

Em Python
```Python
if num <= 0:
    tipo = "não positivo"
else:
    tipo = "positivo"
```

Em Lisp / Clojure
```Clojure
(def tipo (if (<= num 0)
            "não positivo"
            "positivo"))
```


<!-- end_slide -->
# Sintaxe Clojure / Lisp: saída

Em Python
```Python
print(f"media: 7.8")
print("sem newline no final", end='')
```

Em Lisp / Clojure
```Clojure
(println (format "media: %.2f" 7.8))
(print "sem newline no final")
(flush)
```

Em scripts interativos, use `(flush)` após imprimir, para
garantir que a saída seja efetivada imediatamente.


<!-- end_slide -->
# Sintaxe Clojure / Lisp: entrada

Em Python
```Python
nome = input()    # lê string
int(input())      # lê inteiro
float(input())    # lê float
```

Em Lisp / Clojure
```Clojure
(def nome (read-line))
(def n (Integer/parseInt (read-line)))
(def x (Double/parseDouble (read-line)))
```


<!-- end_slide -->
# Sintaxe Clojure / Lisp: usando facilidades Java

Em Lisp / Clojure
```Clojure
(Double/parseDouble (read-line))
(Math/pow num 0.5)
(Math/sin (/ Math/PI 2))
(Math/sqrt 2)
```

Observe que `Double/parseDouble`, `Math/pow` e as demais
operações demonstram a sintaxe Clojure para interoperar com
funções e dados de Java (mais especificamente de `java.lang`) que
implementam essas facilidades. 

Esta é uma das vantagens de Clojure ser uma implementação de Lisp
que é executada na JVM.

<!-- end_slide -->
# Como fazer um main?

Em Python
```Python
def main():
    ...
main()
```

Em Lisp / Clojure
```Clojure
(defn -main [& args]
    ...)
(-main)
```

Idealmente um
programa deve ter um `-main` e o restante do código
em funções independentes (`-main` é apenas um padrão Clojure).
