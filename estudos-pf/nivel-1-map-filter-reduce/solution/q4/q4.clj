(defn len [palavra] 
  (count palavra))

(defn maior? [maior x]
  (if (> maior x) maior x))

(defn pega-maior [sequencia]
  (reduce maior? sequencia))

(defn maior-tamanho [sequencia]
  (pega-maior (map len sequencia)))

(assert (= (maior-tamanho ["a" "bb" "ccc"]) 3))
(assert (= (maior-tamanho ["oi"]) 2))
(assert (= (maior-tamanho ["um" "dois" "tres" "quatro"]) 6))
