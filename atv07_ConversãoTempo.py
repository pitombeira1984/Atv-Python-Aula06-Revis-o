def ConversaoTempo():
    try:
        segundos = int(input("Digite a quantidade de segundos: "))
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos_restantes = (segundos % 3600) % 60
        print(f"{horas}:{minutos}:{segundos_restantes}")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        ConversaoTempo()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
ConversaoTempo()      