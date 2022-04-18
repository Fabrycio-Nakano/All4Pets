import random

class Cliente:
  def __init__(self, nomeUsuario, senha, email, telefone, endereco, id):
    self.nomeUsuario = nomeUsuario=False
    self.__senha = senha
    self.email = email
    self.telefone = telefone
    self.endereco = endereco
    self.id = []

  
  def criarConta(self):
   if self.nomeUsuario == True:
     print(f'{self.nomeUsuario} já existe')
     return
   if len(senha) < 8:
     print('Senha Fraca')
     return
   
   print(f'{self.nomeUsuario} criou a conta com sucesso')  
   self.usuario = True 
   

  def editarPerfil(self):
    if self.nomeUsuario == False:
      print(f'Não existe conta vinculada a esse {self.nomeUsuario}')
      return 
    self.nomeUsuario = str(input('Digite o novo nome de Usuario'))
    
  def trocarSenha(self):
    self.senha = str(input('Digite a nova senha'))
    
    if len(senha) < 8 :
      print("Senha fraca")
      return
      
  def apagarConta(self):
    if self.nomeUsuario == False:
      print(f'Não existe conta vinculada a esse {self.nomeUsuario}')
      return
    self.nomeUsuario == False
    self.senha == False   
    
  def gerarID(self):
    if self.nomeUsuario == False:
      print(f'Conta {self.nomeUsuario} inexistente')
      return   

    self.id = random.sample(range(100), 8)
  
  exit()