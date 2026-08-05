(defn maior-preco-com-desconto [produtos desconto]
  (->> produtos
       (map #(if (> % 100) (* desconto) %))
       (reduce max 0))) 
