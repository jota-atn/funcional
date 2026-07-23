# Pipeline simples: palavra

Usando a biblioteca `result` de Python (instale-a com `pip
install result`), crie um pequeno programa em Python que leia uma
palavra da entrada e que produza **a palavra invertida e em
maiúsculas**, após validar seu conteúdo. A lógica principal deve
ser escrita e empacotada na função `processa(linha: str)`, usando
um pipeline que componha, em estilo monádico, quatro funções
independentes:

- `gritar`: que converte uma string para letras maiúsculas
- `inverter`: que inverte os caracteres de uma string
- `verifica_vogais`: que verifica se a string contém ao menos uma vogal
- `parse_palavra`: que faz a validação da string de entrada

Importante, você deve usar os tipos Ok, Err e Result da
biblioteca result. Você também deve incluir as anotações de tipos
de Python (se precisar, use a biblioteca typing) nas quatro
funções.

As funções devem ser feitas de forma que processem adequadamente
as situações excepcionais, usando objetos do tipo Err com uma
string indicando o erro.

```python
processa("ola")    -> Ok("ALO")
processa("")       -> Err("palavra vazia")
processa("pygmy")  -> Err("sem vogais")
processa("123")    -> Err("caractere inválido")
```
