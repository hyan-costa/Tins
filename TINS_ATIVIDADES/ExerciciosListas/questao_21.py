
modelos = []
consumos = []

for x in range(1, 7):
    print('Veículo %d' % x)
    modelos.append(input('Nome: '))
    consumos.append(float(input('Km por litro: ')))

print('\nRelatório Final')
cont, custo = 0, 0
gasto = consumo = 0
menorModelo = ''
menor = 0
x = 0
for m in modelos:
    custo = 1000 / consumos[cont]
    gasto = custo * 2.25
    x += 1
    print('%d - %s\t- %.1f km/L\t- %.1f litros\t - R$ %.2f' %
          (x, m, consumos[cont], custo, gasto))
    if cont == 0:
        menor = custo
        menorModelo = m
    if menor > custo:
        menor = custo
        menorModelo = m
    cont += 1
print('O menor consumo é do %s.' % (menorModelo))
    

    




    