import hashlib

def cadastrar_usuario():
    #nome = str(input("Digite o seu nome completo: "))
    email = input("Digite o seu endereço de e-mail: ")
    senha = input("Digite a sua senha: ")

    
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

    with open('userCad.txt', 'w') as cadUsers:
        cadUsers.write(f"{email}\n{senha_criptografada}\n")
            
        

    print("Usuário cadastrado com sucesso!")