class Pet:
    def __init__(self,especie,raca,porte,nome):
        self.especie = especie
        self.raca = raca
        self.porte = porte
        self.nome = nome

    def adicionarPet(self, nome, raca, porte, especie):
      
      if ((self.nome and self.raca) and (self.porte and self.especie)) == False:
        print("Digite os campos completos, por favor!")
        return

      x = str(input('Deseja adicionar mais um animal? ')).upper()        #Deixa str em caixa alta
      if x == SIM :                                                      #revisar
        return

      else: 
        print('Adicionado com sucesso!') 
        exit(1)
     
    def  excluirPet(self, nome):
     if self.nome == False: 
       print('Não existe um pet com esse nome!')
       return
      
       self.nome == False
       self.raca == False
       self.porte == False 
       self.especie == False

    def acessarPet(self, nome):
     return self.nome and self.raca and self.porte and self.especie #Retornar tambem informações de serviços