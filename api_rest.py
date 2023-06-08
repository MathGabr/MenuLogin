from bottle import Bottle, request, response, static_file,route,template, run
from pathlib import Path
import json
from truckpad.bottle.cors import CorsPlugin, enable_cors
# https://pypi.org/project/bottle-cors/

app = Bottle()
root = Path(__file__).parent
static_root = root.joinpath('views').joinpath('static')

@route('/static/<filename>')
def static(filename):
    return static_file(filename, root=static_root)

@route('/')
def login():
    return template('login')

def saveUsersInList(user):
    cadastro = listUsers()
    cadastro.append(user)
    with open('backend/cadastro.json','w') as file:
        json.dump(cadastro,file,indent=4)

def listUsers():
    try:
        with open('cadastro.json') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []
    return users

#app.install(CorsPlugin(origins=['*']))

run(host='localhost', port=8081, debug=True, reloader=True)