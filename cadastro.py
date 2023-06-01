from dataclasses import dataclass,asdict
import json
import hashlib

lista_usuarios=[]

@dataclass
class Usuario:
    login: str
    senha: str
    
def cadastrar_usuario():

    email = str(input("Digite o seu endereço de e-mail: "))
    password = str(input("Digite a sua senha: "))

    senha_criptografada = hashlib.sha256(password.encode()).hexdigest()
    usuario_obj = Usuario(login=email, senha= senha_criptografada)

    
    lista_usuarios.append(usuario_obj)

    with open('cadastro.json', 'w') as arquivo:
        lista_usuarios_dict = list(map(asdict, lista_usuarios))
        lista_usuarios_json = json.dumps(lista_usuarios_dict, indent=4)
        arquivo.write(lista_usuarios_json)
        print("Usuário cadastrado com sucesso!\n")

    return usuario_obj
            
        
