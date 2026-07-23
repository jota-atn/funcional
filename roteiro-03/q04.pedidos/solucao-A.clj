(defn total-recebido [dados] 
  (reduce + (map :valor (filter :pago dados))))
