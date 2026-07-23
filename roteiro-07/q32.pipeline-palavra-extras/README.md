# Pipeline simples: palavra (extras)

Comece copiando sua solução para a atividade anterior
(q31.pipeline-palavra) para este diretório. Atualize a função
`processa` para que formate o resultado entre asteriscos (o
resultado passará a ser `**{palavra}**`). Em seguida, adicione a
função `processa_palavras(linhas: list[str])` que recebe uma lista
de strings e que retorna uma lista com cada um dos dados que
tiverem sido processados com sucesso das linhas recebidas.

```python
processa("ola")    -> Ok("**ALO**")
processa("")       -> Err("palavra vazia")
processa("pygmy")  -> Err("sem vogais")

processa_palavras(["ola", "", "abc", "pygmy", "123"])
    -> ["**ALO**", "**CBA**"]
```
