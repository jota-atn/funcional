(defn soma-inteiros [sequencia]
  (if (empty? sequencia)
    0
    (+ (first sequencia) (soma-inteiros (rest sequencia)))))

(assert (= (soma-inteiros [1 2 3 4 5]) 15))
(assert (= (soma-inteiros '(-1 0 1 5 -2)) 3))
(assert (= (soma-inteiros []) 0))
(assert (= (soma-inteiros (range 1 11)) 56))

