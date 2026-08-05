(defn multiplo3? [valor]
  (= (mod valor 3) 0))

(defn soma-multiplo-3 [sequencia]
  (reduce + (filter multiplo3? sequencia)))

(assert (= (soma-multiplo-3 []) 0))
(assert (= (soma-multiplo-3 [1 2 4 5]) 0))
(assert (= (soma-multiplo-3 [3 6 9]) 18))
(assert (= (soma-multiplo-3 [1 3 5 9]) 12))
(assert (= (soma-multiplo-3 [-3 3]) 0))
