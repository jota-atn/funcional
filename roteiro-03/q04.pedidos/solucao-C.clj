(defn total-recebido [dados]
  (transduce (comp (filter :pago) (map :valor)) + 0 dados))
