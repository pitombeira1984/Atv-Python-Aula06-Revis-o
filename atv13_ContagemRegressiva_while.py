def ContagemRegressiva():
    try:
        print("Contagem regressiva")
        i = 10
        while i >= 1:
            print(i)
            i = i - 1
        print("Feliz  Ano Novo!")
    except Exception as e:
        print(f"Erro: {e}")
ContagemRegressiva()