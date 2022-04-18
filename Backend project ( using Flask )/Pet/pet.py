from Conta import conta
from flask import Flask, render_template

class pet:

    def __init__(self, animal, raca, porte, especie):
        self.animal = animal
        self.raca = raca
        self.porte = porte
        self.especie = especie

    @app.route("/adicionarPet")
    def adicionarPet(self, animal):
        if self.animal in ['odin']:
            print("Animal já cadastrado")
            return render_template("adicionarPet.html")

    def acessarPet(self, animal):
        return self.animal and self.raca and self.porte and self.especie

    @app.route("/Pagina_Pet")
    def editarPet(self):
              self.animal = str(input('Digite o nome'))
              self.raca = str(input("Digite a raca"))
              self.porte = str(input('Digite o porte'))
              self.especie = str(input('Digite a especie'))
              print("Edição feita com sucesso")
              print(f'{self.animal}', f'{self.raca}', f'{self.porte}', f'{self.especie}')
              return render_template("adicionarPet.html")

    def excluirPet(self):
        if self.animal not in ['odin']:
            print("Animal não existe")
            return
        else:
            self.animal = None
            self.raca = None
            self.porte = None
            self.especie = None
            print("Animal excluido")

if __name__=="__main__":
  app.run(debug=True)            