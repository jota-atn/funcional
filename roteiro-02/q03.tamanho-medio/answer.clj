(defn tam-medio [palavras]
  (let [validas (filter #(> (count %) 2) palavras)]
    (if (seq validas)
      (/ (reduce + (map count validas)) (count validas))
      0)))
