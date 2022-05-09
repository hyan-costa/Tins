#Faça um programa que mostre os n termos da Série a seguir:
 # S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
n = int(input("Digite n: "))
m = 1
soma = 0
print("S= ", end="")
for x in range(1, n + 1):
    print(f"{x}/{m}", end="")
    
    if x < n and n > 1:
        print(" + ", end="")
    else:
        print(".")
        
    soma += x / m
    m += 2
print(f"soma: %.2f" %soma)