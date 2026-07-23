(defn fatorial
  ([n]
   (fatorial n 1))
  ([n acumulador]
   (if (<= n 1)
     acumulador
     (recur (dec n) (* acumulador n)))))

(assert (= (fatorial 0) 1))
(assert (= (fatorial 1) 1))
(assert (= (fatorial 5) 120))
(assert (= (fatorial 6) 720))
