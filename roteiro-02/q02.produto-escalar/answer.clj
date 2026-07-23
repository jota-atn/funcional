(defn produto-escalar [lista1 lista2]
  (reduce + (map * lista1 lista2)))
