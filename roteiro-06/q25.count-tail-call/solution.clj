(defn meu-count
  ([sequencia]
   (meu-count sequencia 0))
  ([sequencia acumulador]
   (if (empty? sequencia)
     acumulador
     (recur (rest sequencia) (inc acumulador)))))

(assert (= (meu-count []) 0))
(assert (= (meu-count [1 2 3]) 3))
(assert (= (meu-count '(:a :b :c :d)) 4))
(assert (= (meu-count (range 1 11)) 10))
