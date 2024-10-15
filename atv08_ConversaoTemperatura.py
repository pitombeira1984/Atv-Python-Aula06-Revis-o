def ConversaoTemperatura():
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido.")
        ConversaoTemperatura()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
ConversaoTemperatura()
        