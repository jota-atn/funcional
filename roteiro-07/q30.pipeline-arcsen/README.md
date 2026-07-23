# Pipeline simples: arco seno

Usando a biblioteca `result` de Python (instale-a com `pip
install result`), crie um pequeno programa em Python que leia um
número da entrada e que calcule **o quadrado da raiz cúbica do
arco seno** do valor lido. A lógica principal deve ser escrita e
empacotada na função `processa(linha: str)`, usando um pipeline
que componha, em estilo monádico, quatro funções independentes:

- `quadrado`: que calcula o quadrado de um número `n`
- `calcula_raiz_cubica`: que calcula a raiz cúbica de `x`
- `calcula_arco_seno`: que calcula o arco seno (radianos) de `x`
- `parse_float`: que faz o parsing de um float em uma string

Importante, você deve usar os tipos Ok, Err e Result da
biblioteca result. Você também deve incluir as anotações de tipos
de Python (se precisar, use a biblioteca typing) nas quatro
funções.

As funções devem ser feitas de forma que processem adequadamente
as situações excepcionais, usando objetos do tipo Err com uma
string indicando o erro.

```python
processa("0")    -> Ok(0.0)
processa("1")    -> Ok(1.351)
processa("2")    -> Err("arco inválido")
processa("-2")   -> Err("arco inválido")
processa("abc")  -> Err("erro de parsing")
```
