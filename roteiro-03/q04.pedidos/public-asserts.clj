(def pedidos
  [{:cliente "Ana"    :valor 120 :pago true}
   {:cliente "Bruno"  :valor 80  :pago false}
   {:cliente "Ana"    :valor 40  :pago true}
   {:cliente "Carlos" :valor 200 :pago true}
   {:cliente "Bruno"  :valor 30  :pago true}])

(println (total-recebido pedidos))
(assert (= 390 (total-recebido pedidos)))

(println "Tudo ok!")
