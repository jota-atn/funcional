;; private-asserts.clj
(load-file "answer.clj")

(assert (= 10/3 (tam-medio ["casa" "sol" "a" "lua"])))
(assert (= 3 (tam-medio ["ab" "cd" "ef" "ghi"])))

(println "All tests passed!")
