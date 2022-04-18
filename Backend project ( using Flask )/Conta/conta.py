import uuid
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'all'

class conta:

    def __init__(self, nome, senha, id = False ):
     self.nome = nome
     self.senha = senha
     self.id = []

    @app.route("/cadastro")
    def criarConta(self, senha):
        if self.nome in []:            #conferindo se existe um nome de usuario igual no banco de dados! lista vazia recebe qualquer parametro
            print('Conta já existente')
            return render_template("cadastro.html")

        if len(senha) < 8:
            print('Senha Fraca')
            return

        else:
         self.id = uuid.uuid4()          #gerando id aleatorio     # desenvolver metodo para conferir se id é diferente
         print(f'{self.nome} sua conta foi criada e seu  id é {self.id} ')

    @app.route('/editarPerfil', methods=['POST', ])
    def editarPerfil(self):
        if self.nome not in []:                # banco de dados onde sera conferido se existe uma conta igual
             print(f'Não existe conta vinculada ao nome {self.nome}')
             return render_template("editarPerfil.html")

        else:
             self.nome = str(input('Digite o novo nome'))
             print(f'{self.nome} é seu novo nome de usuario')
             return

    @app.route('/editarSenha')
    def trocarSenha(self):
        self.senha = str(input('Digite a nova senha'))

        if len(self.senha) < 8:
            print('Senha Fraca')

        else:
             return redirect('/')


if __name__=="__main__":
