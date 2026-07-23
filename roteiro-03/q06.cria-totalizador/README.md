# Processamento de Eventos

```Clojure
(def eventos
  [{:tipo :compra  :valor 100}
   {:tipo :venda   :valor 50}
   {:tipo :compra  :valor 200}
   {:tipo :taxa    :valor 30}
   {:tipo :venda   :valor 80}])

(def total-compras-e-vendas (cria-totalizador [:compra :venda]))
(total-compras-e-vendas eventos)  ;; => 430
```

No arquivo `resposta.clj`, crie a função `(cria-totalizador
tipos)` que recebe um vetor de tipos e que retorna uma função
que, quando for aplicada a um vetor de eventos, retornará a soma
dos valores associados.

tipos eventos)` que recebe um vetor de eventos (mapas) de um
sistema de comercial com dados no formato visto e que retorna a
soma dos valores dos tipos contidos na sequência `tipos` (veja o
exemplo acima e o arquivo `public-asserts.clj`.

Restrições:
- use `comp` para compor transformações reusáveis
- use `partial` como forma de especializar funções

Dica. Para resolver, pense em termos de um pipeline: eventos -> filtrar
-> extrair valores -> somar.
