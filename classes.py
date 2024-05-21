class Pessoa():
    def __init__(self, nome, idade, peso) :
        self.nome = nome
        self.idade = idade
        self.peso = peso

        self.dormindo = False
        self.falando = False
        self.comendo = False

    def comer (self, comida):
        if self.dormindo == True:
            print(f"{self.nome}-Não pode comer porque está dormindo")
        elif(self.falando == True):
            print(f" {self.nome}'Não pode comer porque está falando")
        else:
            self.comendo = True
            print(f' {self.nome} está comendo {comida}.')
    def pararComer(self):
        print("Parei de comer")

    def falar(self,fala):
        if (self.dormindo == True):
            print(f" (self,nome)-Não pode falar porque está dormindo")
        elif(self.comendo == True):
            print(f" {self.nome} Não pode falar porque está Comendo")
        else:
            self.falando = True
            print (f"{self.nome} está falando {fala}.")
    def pararFalar(self):
        print("Parei de falar!!")
    def dormir(self):
        print("Vou dormir...")
    def pararDormir(self):
        print("Acordei..")
    
    