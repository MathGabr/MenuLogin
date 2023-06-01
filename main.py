from cadastro import cadastrar_usuario
from login import realizar_login


while True:
    print("MENU")
    print("1. Realizar o cadastro de usuários")
    print("2. Realizar login")
    print("3. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        realizar_login()
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite uma opção válida.")
    
