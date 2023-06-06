from dataclasses import dataclass,asdict
import json
import hashlib

lista_usuarios=[] 

@dataclass
class Usuario:
    login: str
    senha: str
    
def cadastrar_usuario():
    email = str(input("\nDigite o seu endereço de e-mail: "))
    password = str(input("Digite a sua senha: "))

    senha_criptografada = hashlib.sha256(password.encode()).hexdigest()

    usuario_obj = Usuario(login=email, senha= senha_criptografada)#cria o obj do usuario
    lista_usuarios.append(usuario_obj) #adiciona o obj a lista

    with open('cadastro.json', 'w') as arquivo:
        lista_usuarios_dict = list(map(asdict, lista_usuarios))# de lista str para dict
        lista_usuarios_json = json.dumps(lista_usuarios_dict, indent=4) #de dict para json
        arquivo.write(lista_usuarios_json)#registra
        print("\nUsuário cadastrado com sucesso!\n")

    return usuario_obj#retorno para a felicidade do coverage
            
        
