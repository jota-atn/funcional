(defn fatorial [n]
  (if (<= n 1)
    1
    (* n (fatorial (dec n)))))

(assert (= (fatorial 0) 1))
(assert (= (fatorial 1) 1))
(assert (= (fatorial 5) 120))
(assert (= (fatorial 6) 720))
