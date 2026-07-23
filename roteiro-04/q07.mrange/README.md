# Range Infinito

O `range` de python não tem a mesma semântica do seu equivalente
em Clojure. Pede-se que você implemente uma função _wrapper_ para
`range` chamada `mrange` que tenha exatamente a mesma semântica
que `range` de Clojure. Observe que a questão pede que você faça
um _wrapper_! Ou seja, você pode usar `range` para implementar
`mrange`.

Atenção! O aspecto mais importante aqui é fazer com que `mrange`
aceite ser invocado sem argumentos. Nesse caso, ele deve retornar
uma sequência infinita de inteiros começando do zero (lazy, é
claro)
