# Pipeline simples

Usando a biblioteca `result` de Python (instale-a com `pip
install result`), crie um pequeno programa em Python que leia um
número da entrada e que calcule **o dobro do inverso da raíz
quadrada** do valor lido. A lógica principal deve ser escrita e
empacotada na função `processa(linha: str)`, usando um pipeline
que componha, em estilo monádico, quatro funções independentes: 

- `dobro`: que calcula o dobro de um número `n`
- `calcula_inverso`: que calcula o valor inverso (`1 / x`)
- `calcula_raiz`: que calcula a raiz quadrade de `x`
- `parse_float`: que faz o parsing de um float em uma string

Importante, você deve usar os tipos Ok, Err e Result da
biblioteca result. Você também deve incluir as anotações de tipos
de Python (se precisar, use a biblioteca typing) nas quatro
funções. 

As funções devem ser feitas de forma que processem adequadamente
as situações excepcionais, usando objetos do tipo Err com uma
string indicando o erro.

```python
processa("16")   -> Ok(0.5)
processa("-4")   -> Err("erro na raiz")
processa("0")    -> Err("divisão por zero")
processa("abc")  -> Err("erro de parsing")
```
