(defn total-recebido [pedidos]
  (->> pedidos
       (filter #(:pago %))
       (map #(:valor %))
       (reduce +)))
