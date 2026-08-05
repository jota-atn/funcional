(def numeros-infinitos (range))

(defn multiplos-5 [numeros]
  (map #(* 5 %) numeros))

(def infinitos-multiplos (multiplos-5 numeros-infinitos))
