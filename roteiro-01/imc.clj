(defn le-peso []
  (print "Informe o seu peso: ")
  (flush)
  (let [peso (parse-double (read-line))] peso)
  )

(defn imc [peso]
  (cond
      (< peso 18.5) "Abaixo do peso"
      (< peso 25.0) "Peso normal"
      (< peso 30.0) "Sobrepeso"
      (< peso 35.0) "Obesidade grau I"
      (< peso 40.0) "Obesidade grau II"
      :else "Obesidade grau III"
    )
  )

(defn -main []
  (let [peso (le-peso)] (println (imc peso)))
  )

(-main)
