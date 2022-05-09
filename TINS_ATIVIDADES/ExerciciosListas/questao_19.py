import numbers
from operator import index
num_system = []
entrada = 0

while entrada >= 1 or entrada <= 6:

    entrada = int(input("1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\n"))

    #finaliza o a execução
    if entrada == 0:
        break
    
    num_system.append(entrada)
# sistema recebe todos os elementos da lista num_system exeto os maiores que 6 e inferiores a 1
sistema = [num_system for num_system in num_system if num_system<=6 and num_system>=1]

#as variaveis abaixo recebe a porcentagem de dos votos de cada sistema
p1 = sistema.count(1)/len(sistema) * 100
p2 = sistema.count(2)/len(sistema) * 100
p3 = sistema.count(3)/len(sistema) * 100
p4 = sistema.count(4)/len(sistema) * 100
p5 = sistema.count(5)/len(sistema) * 100
p6 = sistema.count(6)/len(sistema) * 100
#armazena o total de votos de cada sistema
contagem = [
    sistema.count(1),
    sistema.count(2),
    sistema.count(3),
    sistema.count(4),
    sistema.count(5),
    sistema.count(6)
]
#o dicionario facilita chamar o sistema que mais foi votado
val_system = {
    "windows server":p1,
    "unix":p2,
    "linux":p3,
    "netware":p4,
    "mac os":p5,
    "outro":p6
}

max_key = max(val_system, key = val_system.get)

print("\nSitema Operacional \tVotos   %")
print('------------------  \t-----   ----')
print(f'Windows Server \t\t{sistema.count(1)} ' + '\t%.2f%%' % p1)
print(f'Unix      \t\t{sistema.count(2)} ' + '\t%.2f%%' % p2)
print(f'Linux     \t\t{sistema.count(3)} ' + '\t%.2f%%' % p3)
print(f'Netware   \t\t{sistema.count(4)} ' + '\t%.2f%%' % p4)
print(f'Mac OS    \t\t{sistema.count(5)} ' + '\t%.2f%%' % p5)
print(f'Outro     \t\t{sistema.count(6)} ' + '\t%.2f%%' % p6)
print('------------------  \t-----   ----')
print(f'Total      \t\t{len(sistema)}\n')

print("sistema operacional mais votado foi o ",max_key," com %.2f"%val_system[max_key],
      "%. Totalizando ", max(contagem)," de votos")



