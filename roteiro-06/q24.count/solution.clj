(defn meu-count [sequencia]
  (if (empty? sequencia)
    0
    (+ 1 (meu-count (rest sequencia)))))

(assert (= (meu-count []) 0))
(assert (= (meu-count [1 2 3]) 3))
(assert (= (meu-count '(:a :b :c :d)) 4))
(assert (= (meu-count (range 1 11)) 10))
