import hashlib

def realizar_login():
    email = input("Digite o seu endereço de e-mail: ")
    senha = input("Digite a sua senha: ")

    
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

    
    with open('userCad.txt', 'r') as arquivo:
        linhas = [linha.rstrip() for linha in arquivo.readlines()]
        if email in linhas and senha_criptografada == linhas[linhas.index(email) + 1]:
            print("Login efetuado com sucesso!")
        else:
            print("Email ou senha incorretos.")

    #precisa fazer como no arquivo do moodle da materia de engenharia de software cujo nome do arquivo é: CaioArquivo