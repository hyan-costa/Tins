class pessoa:
    def __init__(self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def engorda(self, kilo):
        self.peso += kilo
        return self.peso
    
    def emagrecer(self, kilo):
        self.peso -= kilo
        return self.peso
    
    def crescer(self, anos):
        if self.idade <=21:
            self.altura += (0.05 * anos)
        return self.altura

    def envelhecer(self, anos):
        self.idade +=anos
        return self.idade
    
nome=input("digite seu nome:")
idade = int(input("digite sua idade"))
altura = float(input("digite sua altura"))
peso = float(input("digite seu peso"))

p1 = pessoa(nome,idade,altura,peso)

print("nome:",p1.nome,"\tidade: ",p1.idade,"\taltura: ",p1.altura,"\tpeso: ",p1.peso,"\n"*4)

anos = float(input("quantos anos se passaram?"))
engordar = float(input("engordou quantos kilos?"))
emagrecer = float(input("emagreceu quantos kilos?"))

p1.crescer(anos)
p1.engorda(engordar)
p1.emagrecer(emagrecer)
p1.envelhecer(anos)

print("\nnome:",p1.nome,"\tidade: ",p1.idade,"\taltura:%.2f "%p1.altura,"\tpeso: ",p1.peso)

        
        
        
        