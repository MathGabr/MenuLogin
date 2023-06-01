import unittest
from unittest.mock import patch
from cadastro import *
from login import *

class MainTest(unittest.TestCase):

    @patch('builtins.input', lambda *args: 'ettore')
    def test_cadastrar_usuario(self):
        inputs = iter([
            'ettore',
            'senha'
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            usuario = cadastrar_usuario()
            self.assertEqual(usuario.login, 'ettore')
            self.assertEqual(usuario.senha, hashlib.sha256('senha'.encode()).hexdigest())


    def test_realizar_login(self):
        inputs = iter([
            'ettore',
            'senha',
            'doce',
            'salgado'
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            usuario = realizar_login()
            self.assertEqual(usuario.login, 'ettore')
            self.assertEqual(usuario.senha, hashlib.sha256('senha'.encode()).hexdigest())
            usuario = realizar_login()
            self.assertIsNone(usuario)
            
