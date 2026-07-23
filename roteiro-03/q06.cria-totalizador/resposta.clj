(defn cria-totalizador [tipos]
  (let [
        filtrar-por-tipo (partial filter (fn [e] (some #(= (:tipo e) %) tipos)))
        extrair-valores (partial map :valor)
        somar (partial reduce + 0)]
    
    (comp somar extrair-valores filtrar-por-tipo)))
