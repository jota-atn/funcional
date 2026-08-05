(defn positivo [numero]
  (> numero 0))

(defn positivos [numeros]
  (filter positivo numeros))

(defn produto-positivos [sequencia]
  (reduce * (positivos sequencia)))

(assert (= (produto-positivos []) 1))
(assert (= (produto-positivos [-1 -2]) 1))
(assert (= (produto-positivos [2 3 -1]) 6))
(assert (= (produto-positivos [1 2 3 4]) 24))
