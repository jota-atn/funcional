;; list(map(lambda n: n * 10, filter(lambda n: n > 0, numeros)))

(defn comprehension [lambda sequencia filtro]
  (for [n sequencia :when (filtro n)] (lambda n)))

(println (comprehension #(* % 10) '(-2 -1 0 1 2) #(> % 0)))


  
