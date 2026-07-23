;; asserts.clj
(load-file "answer.clj")

(assert (= 56 (processa [2 4 6])))
(assert (= 4 (processa [1 2 3])))

(println "Tudo ok!")
