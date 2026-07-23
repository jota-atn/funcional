# Processamento de Eventos

```Clojure
(def eventos
  [{:tipo :compra  :valor 100}
   {:tipo :venda   :valor 50}
   {:tipo :compra  :valor 200}
   {:tipo :taxa    :valor 30}
   {:tipo :venda   :valor 80}])

(total-filtrado [:compra :venda] eventos)   ;; => 430
```

No arquivo `resposta.clj`, crie a função `(total-filtrado
tipos eventos)` que recebe um vetor de eventos (mapas) de um
sistema de comercial com dados no formato visto e que retorna a
soma dos valores dos tipos contidos na sequência `tipos` (veja o
exemplo acima e o arquivo `public-asserts.clj`.

Restrições:
- use `comp` para compor transformações reusáveis
- use `partial` como forma de especializar funções

Dica. Para resolver, pense em termos de um pipeline: eventos -> filtrar
-> extrair valores -> somar.
