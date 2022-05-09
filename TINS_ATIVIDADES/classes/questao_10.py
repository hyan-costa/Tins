class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litroAbastecido = valor/self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - litroAbastecido)
        return litroAbastecido

    def abastecerPorLitro(self, qtd):
        temp2 = qtd * self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - qtd)
        return temp2


a1 = BombaCombustivel("Gasolina", 7, 500)
a1.alterarCombustivel("etanol")
print("------abastecimento por valor R$------")
print("total de combustivel na bomba: %.3f"% a1.quantidadeCombustivel, "L")
print("foi abastecido: %.3f"% a1.abastecerPorValor(150),'L')
print("sobrou na bomba: %.3f"% a1.quantidadeCombustivel,'L\n\n')
print("----------abastecimento por litro---------")
print("total a pagar: %.2f"% a1.abastecerPorLitro(30),'Reais')
print("sobrou na bomba: %.3f"% a1.quantidadeCombustivel,'L')
