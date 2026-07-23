# Pedidos

```Clojure
(def pedidos
  [{:cliente "Ana"    :valor 120 :pago true}
   {:cliente "Bruno"  :valor 80  :pago false}
   {:cliente "Ana"    :valor 40  :pago true}
   {:cliente "Carlos" :valor 200 :pago true}
   {:cliente "Bruno"  :valor 30  :pago true}])
```

A. No arquivo `solucao-A.clj` escreva apenas a função `total-recebido`
que recebe um vetor de pedidos (que por sua vez são mapas) no mesmo
formato ao que se vê acima e que retorna o valor total de pedidos pagos.
Escreva usando funções de alta ordem, sem usar nem mutabilidade, nem
recursividade.

B. No arquivo `solucao-B.clj` reescreva a função, em estilo _pipeline_,
usando a macros `->>` (_threading_) de Clojure.

C. No arquivo `solucao-C.clj` reescreva mais uma vez a função, desta vez
usando a função `comp` de composição, de Clojure.

D. No arquivo `solucao-D.clj` reescreva novamente a função, desta vez
usando a função de composição `partial`.
