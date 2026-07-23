(defn total-filtrado [tipos eventos]
  (let [
        filtrar (partial filter (fn [e] (some #(= (:tipo e) %) tipos)))
        extrair (partial map :valor)
        somar (partial reduce + 0)
        pipeline (comp somar extrair filtrar)]
    
    (pipeline eventos)))
