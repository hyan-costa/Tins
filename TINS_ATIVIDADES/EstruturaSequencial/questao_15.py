#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.

salario = float(input("digite o quanto voce ganha por hora: "))
horas = int(input("digite quantas horas voce trabalha no mês: "))

salBruto = float(salario * horas)

impRenda = (11 * salBruto) / 100
inss = (8 * salBruto) / 100
sindiato = (5 * salBruto) / 100

salLiquido = ( ( (salBruto - impRenda) - inss) - sindiato) 

print("\nsalario bruto: R$ %.2f" %  salBruto)
print("\ninss: R$ %.2f" % inss)
print("\nsindicato: R$ %.2f" % sindiato)
print("\nsalario liquido: R$ %.2f" % salLiquido)