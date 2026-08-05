;; [n.upper() for n in palavras if len(n) > 3]

(require '[clojure.string :as str])

(defn capitaliza-maior-que-3 [sequencia]
  (for [palavra sequencia :when (> (count palavra) 3)] (str/upper-case palavra)))

(defn map-filter-capitaliza-maior-que-3 [sequencia]
  (map str/upper-case (filter #(> (count %) 3) sequencia)))

(println (capitaliza-maior-que-3 '("oi" "fala")))
(println (map-filter-capitaliza-maior-que-3 '("oi" "fala")))
