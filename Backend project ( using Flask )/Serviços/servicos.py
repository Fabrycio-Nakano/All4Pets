from Empresa import empresa
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'all'

class servicos:

    def __init__(self, empresa, telefone, preco, tipo):     #tipo = tipoServiço
        self.empresa = []
        self.telefone = []
        self.preco = []
        self.tipo = []

    @app.route("/Busca")
    def indicarPrestadora(self, tipo):
        for self.tipo in self.empresa:
            if self.tipo in self.empresa:
                print(f'{self.empresa}')
            return self.empresa and render_template("Busca.html")

    @app.route("/Busca_Preço")
    def consultaPreco(self, tipo):
        for self.tipo in self.preco:
            return self.preco and render_template("Buscapreco.html")

    def requisitarServico(self, tipo):
        for self.tipo in self.empresa:
            return self.empresa
            rs = str(input("Deseja selecionar serviço? S/N"))
            if rs == 'S':
                self.tipo = []
                self.empresa = []
            else:
                return

    def pesquisaEmpresa(self,tipo, empresa = False):
        if self.tipo not in []:
            print("Infelizmente nenhum parceiro presta esse tipo de serviço")
        else:
            for self.tipo in self.empresa:
                return self.empresa
                
if __name__=="__main__":
  app.run(debug=True)