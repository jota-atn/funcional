(ns your-app.core
    (:require [clojure.math :as math]))

(defn delta [a b c]
  (println "calculando delta")
  (- (* b b) (* 4 a c)))

(defn raizes [a b c]
  (let [valor_delta (delta a b c)] 
    (cond
      (< valor_delta 0.0) []
      (= valor_delta 0)  (let [x1 (/ (+ (- b) (math/pow valor_delta 0.5)) (* 2 a))] [x1])
      :else (let [x1 (/ (+ (- b) (math/pow valor_delta 0.5)) (* 2 a))
                  x2 (/ (- (- b) (math/pow valor_delta 0.5)) (* 2 a))] [x1 x2])
      )))

(defn le_coeficiente [nome_coeficiente]
  (println (str "Digite o coeficiente " nome_coeficiente))
  (let [linha (read-line)] (parse-double linha))
  )

(defn main []
  (println "Resolvedor de equações quadráticas: ax² + bx + c = 0\n")  
  (let [a (le_coeficiente "a")
        b (le_coeficiente "b")
        c (le_coeficiente "c")]
    (cond 
      (= a 0.0) (println "\nErro: 'a' não pode ser zero em uma equação quadrática")
      :else (let [valor_delta (delta a b c)
                  raizes_result (raizes a b c)
                  x1 (cond (> (count raizes_result) 0) (nth raizes_result 0) :else nil)
                  x2 (cond (> (count raizes_result) 1) (nth raizes_result 1) :else nil)]
              (println (str "\nΔ = " valor_delta))
              (println x1)
              (println x2)
              )
      ))
  )

(main)
