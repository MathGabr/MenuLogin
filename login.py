import hashlib
import json
from cadastro import Usuario

def realizar_login():
    email = input("\nDigite o seu endereço de e-mail: ")
    senha = input("Digite a sua senha: ")

    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()


    def dict_to_usuario(d):
        return Usuario(**d)

    with open('cadastro.json', 'r') as arquivo:
        lista_usuarios_json = arquivo.read()#le o arquivo e transforma em variavel
        lista_usuarios_dict = json.loads(lista_usuarios_json)#converte de json para dict
        lista_usuarios = list(map(dict_to_usuario, lista_usuarios_dict))#de dict em lista

        for usuario in lista_usuarios:#confere se os valores inseridos estão registrados
            if email == usuario.login and senha_criptografada == usuario.senha:
                print("\nlogin feito com sucesso!\n")
                return usuario
        print("\nusuario desconhecido ;-;\n")