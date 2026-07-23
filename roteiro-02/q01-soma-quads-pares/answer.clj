(defn processa [lista]
  (reduce + 0 (map #(* % %) (filter even? lista)))) 
