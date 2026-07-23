(defn soma-inteiros
  ([sequencia]
   (soma-inteiros sequencia 0))
  ([sequencia acumulador]
   (if (empty? sequencia)
     acumulador
     (recur (rest sequencia) (+ acumulador (first sequencia))))))

(assert (= (soma-inteiros [1 2 3 4 5]) 15))
(assert (= (soma-inteiros '(-1 0 1 5 -2)) 3))
(assert (= (soma-inteiros []) 0))
(assert (= (soma-inteiros (range 1 11)) 55))
