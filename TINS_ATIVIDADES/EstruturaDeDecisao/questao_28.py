carne = ""
valor = float()
desconto = float()

carnes = {
    1 : "filé duplo",
    2 : "alcatra",
    3 : "picanha"
}

def cupom():
    carne = carnes[escolha]
    print("\n\n----cupom fiscal----") 
    print("----tipo de carne:",carne)
    print("----peso:",peso,"kilos")
    print("----catao tabajara:",cartao)
    print("----desconto:R$ %.2f" % desconto)
    print("----total:R$ %.2f" % total)


print("digite um dos segunites números para escolher a carne: ")
escolha = int(input("\n1 : para filé duplo. \n2 : para alcatra. \n3 : para picanha.\n"))
peso = float(input("quantos quilos? "))
cartao = input("usará o cartão tabajara nessa compra? (sim/nao)\n")


match escolha:
    case 1:
        if peso <= 5:
            valor = peso * 4.90
        else:
            valor = peso * 5.80
    case 2:
        if peso <=5:
            valor = peso * 5.90
        else:
            valor = peso * 6.80
    case 3:
        if peso <= 5:
            valor = peso * 6.90
        else:
            valor = peso * 7.80
    case _:
        print("erro ao processar informação")
        
#caso use o catão terá desconto de 5%
if cartao == 'sim':
    desconto = ((valor * 5)/100)
    total = valor - desconto
    cupom()
#caso nao use o catão
elif cartao == 'nao':
    total = valor
    cupom()
else:
    print("erro ao processar informação")









        
    