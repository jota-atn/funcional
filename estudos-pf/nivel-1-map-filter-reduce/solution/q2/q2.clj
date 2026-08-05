(defn negativo? [numero]
  (if (< numero 0) 
        1
        0))

(defn conta_negativos [numeros]
  (reduce + (map negativo? numeros)))

(assert (= (conta_negativos []) 0))
(assert (= (conta_negativos [1 2 3]) 0))
(assert (= (conta_negativos [-1 -2 3]) 2))
(assert (= (conta_negativos [0 -5]) 1))
