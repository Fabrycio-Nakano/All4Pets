from Conta import conta
from datetime import datetime, date, time
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'all'



class Parceiros:
    def __init__(self, razaoSocial, cnpj, telefone, tipo, email, data, hora):
        self.razaoSocial = []
        self.cnpj = cnpj
        self.telefone = telefone
        self.tipoServico = tipo
        self.email = email
        self.data = data
        self.hora = hora

   @app.route("/Parceiros")
    def mostrarServico(self, tipo):
        index_i = 0
        index_j = 0

        for i in range(len(razaoSocial)):  # procurar no array razaoSocial
            for j in range(i):  # procurar em todos os elementos nessa lista
                if elemento in lista[i][j]:  # encontrando elemento generico ('tipoServiço')
                    index_i = i
                    index_j = j
                    break
                break
        return (index_i, index_j) and render_template("Parceiros.html")  # retornando os índices

        print(razaoSocial[index_i][index_j])

    def agendamento(self, nomeUsuario, razaoSocial, data, hora):
        return self._data  # Repensar!
    
if __name__=="__main__":
  app.run(debug=True)