import math

def delta(a, b, c):
    """Calcula o delta (discriminante) da equação ax² + bx + c = 0"""
    print("calculando delta")
    return b * b - 4 * a * c

def raizes(a, b, c):
    """Calcula as raízes reais x1 e x2 a partir de a, b e c"""
    vdelta = delta(a, b, c)
    if vdelta < 0.0:
        return []
    x1 = (-b + math.pow(vdelta, 0.5)) / (2 * a)
    x2 = (-b - math.pow(vdelta, 0.5)) / (2 * a)
    if vdelta == 0.0:
        return [x1]
    return [x1, x2]

def le_coeficiente(nome_coeficiente):
    """Lê um coeficiente da equação da entrada padrão com um prompt"""
    linha = input(f"Digite o coeficiente {nome_coeficiente}: ")
    return float(linha.strip())

def main():
    """Função main do resolvedor de equações quadráticas"""
    print("Resolvedor de equações quadráticas: ax² + bx + c = 0\n")
    a = le_coeficiente("a")
    b = le_coeficiente("b")
    c = le_coeficiente("c")
    if a == 0:
        print("\nErro: 'a' não pode ser zero em uma equação quadrática")
    else:
        vdelta = delta(a, b, c)
        raizes_result = raizes(a, b, c)
        x1 = raizes_result[0] if len(raizes_result) > 0 else None
        x2 = raizes_result[1] if len(raizes_result) > 1 else None
        print(f"\nΔ = {vdelta:.2f}")
        if x1 is not None:
            print(f"x₁ = {x1:.2f}")
        if x2 is not None:
            print(f"x₂ = {x2:.2f}")

if __name__ == "__main__":
    main()
