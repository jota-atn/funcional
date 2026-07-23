(def total-recebido
  (comp (partial reduce +)
        (partial map #(:valor %))
        (partial filter #(:pago %))))
