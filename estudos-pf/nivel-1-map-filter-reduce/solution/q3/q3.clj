(defn quadrados [sequencia]
  (map #(* % %) sequencia))

(defn pares [sequencia]
  (filter even? sequencia))

(defn soma-quadrados-pares [sequencia] 
  (reduce + (quadrados (pares sequencia))))

(assert (= (soma-quadrados-pares []) 0))
(assert (= (soma-quadrados-pares [1 3 5]) 0))
(assert (= (soma-quadrados-pares [1 2 3 4]) 20))
(assert (= (soma-quadrados-pares [-2 3]) 4))
