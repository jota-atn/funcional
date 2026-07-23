(defn fibonacci
  ([n]
   (fibonacci n 0 1))
  ([n atual proximo]
   (if (zero? n)
     atual
     (recur (dec n) proximo (+ atual proximo)))))

(assert (= (fibonacci 0) 0))
(assert (= (fibonacci 1) 1))
(assert (= (fibonacci 2) 1))
(assert (= (fibonacci 3) 2))
(assert (= (fibonacci 4) 3))
(assert (= (fibonacci 5) 5))
(assert (= (fibonacci 6) 8))
(assert (= (fibonacci 7) 13))
