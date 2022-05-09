#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("digite S para sim e N para não.")
cont_result = 0
pergunta = [
    "telefonou para vítima? ",
    "esteve no local do crime? ",
    "mora perto da vítima? ",
    "devia para a vítima? ",
    "já trabalhou com a vítima? "
]

resultado = {
    0 : "inocente",
    2 : "suspeito",
    3 : "cumplice",
    4 : "cumplice",
    5 : "assasino",
}

#percorre o a lista pergunta e soma 1 a variavel cont_result caso a resposta for sim
for cont_pergunta in range(len(pergunta)):
    print(pergunta[cont_pergunta])
    resp = input()
    
    if resp == 's' or resp =='S':
        cont_result+=1
#printa o valor armazenado na posiçao cont_result no dicionario resultado   
if cont_result in resultado:
  print(resultado[cont_result])