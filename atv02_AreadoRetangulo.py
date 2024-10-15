def AreadoRetangulo():
    try:
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"A área do retângulo é: {area}")
        return area
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        return AreadoRetangulo(area)
AreadoRetangulo()
    