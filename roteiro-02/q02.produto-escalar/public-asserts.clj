(load-file "answer.clj")

(assert (= 32 (produto-escalar [1 2 3] [4 5 6])))
(assert (= -10 (produto-escalar [2 -3] [4 6])))

(println "Tudo ok!")
