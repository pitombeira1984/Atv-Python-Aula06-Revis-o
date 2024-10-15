def SistemaLogin():
    try:
        print("Bem-vindo ao Sistema de Login!")
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        if usuario == "admin" and senha == "123":
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        SistemaLogin()
    finally:
        print("Fim do Programa")
SistemaLogin()