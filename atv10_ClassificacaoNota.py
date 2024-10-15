def ClassificacaoNota():
    try:
        nota = float(input("Digite a nota: "))
        if nota >= 90:
            print("A")
        elif nota >= 80:
            print("B")
        elif nota >= 70:
            print("C")
        elif nota >= 60:
            print("D")
        else:
            print("F")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
        ClassificacaoNota()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
ClassificacaoNota()