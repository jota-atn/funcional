(defn soma-notas-aprovados [turmas N media-min]
  (->> turmas
       (filter #(>= (count %) N))
       (map #(/ (reduce + %) (count %)))
       (filter #(>= % media-min))
       (reduce + 0)))
