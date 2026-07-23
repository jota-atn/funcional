(def eventos
  [{:tipo :compra  :valor 100}
   {:tipo :venda   :valor 50}
   {:tipo :compra  :valor 200}
   {:tipo :taxa    :valor 30}
   {:tipo :venda   :valor 80}])

(def total-compras-e-vendas (cria-totalizador [:compra :venda]))
(def total-vendas-e-taxas (cria-totalizador [:venda :taxa]))

(assert (= 430 (total-compras-e-vendas eventos)))
(assert (= 160 (total-vendas-e-taxas eventos)))
