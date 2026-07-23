(def eventos
  [{:tipo :compra  :valor 100}
   {:tipo :venda   :valor 50}
   {:tipo :compra  :valor 200}
   {:tipo :taxa    :valor 30}
   {:tipo :venda   :valor 80}])

(assert (= 430 (total-filtrado [:compra :venda] eventos)))
(assert (= 160 (total-filtrado [:venda :taxa] eventos)))
