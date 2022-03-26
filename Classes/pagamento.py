from datetime import datetime
from random import random
from cliente import Cliente
from parceiros import parceiros
from servicos import servicos


class Conta:
    def __init__(self, nomeUsuario, senha, email, dataNascimento):
        self._nomeUsuario = nomeUsuario
        self._senha = senha
        self._dateRemove = 0
        self._autorizarserviço = None
        self._numero = numero
        self._cvv = cvv
        self.vencimento = vencimento
        self._perfil = Perfil(random(), nomeUsuario, email, dataNascimento)

    @property
    def perfil(self):
        return self._perfil

    @property
    def Cadastrocartao(self, numero, cvv, vencimento):    
        return self._Cadastrocartao

    @property
    def Autorizarservico(self, bancoaut=None):                                       #Solicitando acesso ao pagamento atraves do banco
        if bancoaut is not None:
         return self._bancoaut 

    @property
    def EditarPerfilPagamento(self, nome=None, email=None, dataNascimento=None, foto=None):
        if nome is not None:
            self._perfil.nome = nome
        if email is not None:
            self._perfil.email = email
        if dataNascimento is not None:
            self._perfil.dataNascimento = dataNascimento
        if nome is not None:
            self._perfil.foto = foto

    def RemoverPerfil(self, nomeUsuario, senha):
        if (nomeUsuario == self._nomeUsuario) and (senha == self._senha):
            self._perfil.showStatus = False
            self._dateRemove = datetime.today()                                  #função que apaga do banco de dados após 30 dias
                                                                                  
                                                                                  
    def RecuperarPerfil(self, nomeUsuario, senha):
        if (nomeUsuario == self._nomeUsuario) and (senha == self._senha):
            self._perfil.showStatus = True
            self._dateRemove = 0