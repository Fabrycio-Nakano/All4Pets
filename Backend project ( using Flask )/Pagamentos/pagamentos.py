from datetime import datetime
from random import random
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'all'

class Pagamento:
    def __init__(self, nome, senha, email, dataNascimento):
        self._nome = nome
        self._senha = senha
        self._dateRemove = 0
        self._autorizarserviço = None
        self._numero = numero
        self._cvv = cvv
        self.vencimento = vencimento
        self._perfil = Perfil(random(), nome, email, dataNascimento)

    @property
    def perfil(self):
        return self._perfil

    @property
    @app.route("/Cadastrocartão")
    def Cadastrocartao(self, numero, cvv, vencimento):
        return self._Cadastrocartao  #return em erro! Verificar. 

    @property
    def Autorizarservico(self, bancoaut=None):  # Solicitando acesso ao pagamento atraves do banco
        if bancoaut is not None:
            return self._bancoaut

    @property
    @app.route("/Pagamento")
    def EditarPerfilPagamento(self, nome=None, email=None, dataNascimento=None, foto=None):
        if nome is not None:
            self._perfil.nome = nome
        if email is not None:
            self._perfil.email = email
        if dataNascimento is not None:
            self._perfil.dataNascimento = dataNascimento
        if nome is not None:
            self._perfil.foto = foto
            return  render_template("Pagamento.html")

    @app.route("/Perfilpagamento")
    def RemoverPerfil(self, nome, senha):
        if (nomeUsuario == self._nome) and (senha == self._senha):
            self._perfil.showStatus = False
            self._dateRemove = datetime.today()  # função que apaga do banco de dados após 30 dias
            return render_template("/Pagamento")

    def RecuperarPerfil(self, nome, senha):
        if (nomeUsuario == self._nome) and (senha == self._senha):
            self._perfil.showStatus = True
            self._dateRemove = 0
            
if __name__=="__main__":
  app.run(debug=True)
