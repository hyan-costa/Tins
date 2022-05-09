#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
#-------------------------------------------------------------------------------------------------------------
sexo = input("digite M para masculino ou F para feminino: ")

#calculo masculino
if sexo == 'M' or sexo == 'm' :
   altura =  float(input("digite sua altura: "))
   mmc = float(( altura * 72.7) - 58.0)
   print("seu peso ideal é: %.3f" % mmc, "kg")


#calculo feminino  
elif sexo == 'F' or sexo == 'f' :
   altura =  float( input("digite sua altura: "))
   mmc = float(( altura * 62.1) - 44.7)
   print("seu peso ideal é: %.3f" % mmc, "kg")

else :
    print("erro!!")  