from cliente import cliente
from datetime import datetime, date, time

class Parceiros:
    def __init__(self,razaoSocial,cnpj,telefone,tipoServico,email,data, hora):
        self.razaoSocial = []
        self.cnpj = cnpj
        self.telefone = telefone
        self.tipoServico = tipoServico
        self.email = email
        self.data = data
        self.hora = hora
        

    def indicacaoServico(self, tipoServico):
        index_i = 0 
        index_j = 0 

        for i in range (len(razaoSocial)): # procurar no array razaoSocial
          for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # encontrando elemento generico ('tipoServiço')
                index_i = i 
                index_j = j
                break 
            break 
        return (index_i, index_j) # retornando os índices

        print(razaoSocial[index_i][index_j])

    def agendamento(self, nomeUsuario, razaoSocial, data, hora): 
       return self._data