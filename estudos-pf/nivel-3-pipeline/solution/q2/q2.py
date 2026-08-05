def maior_preco_com_desconto(produtos: list, DESCONTO: float) -> float:
    produtos_desconto = [n * DESCONTO if n >= 100 else n for n in produtos]
    return max(produtos_desconto, default=0)

print(maior_preco_com_desconto([], 0.1))
print(maior_preco_com_desconto([50, 80], 0.1))
