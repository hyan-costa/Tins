#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input("nota 01: "))
nota_2 = float(input("nota 02: "))
media = float((nota_1 + nota_2) / 2)

if nota_1 < 11 and nota_2 < 11:
    if media == 10:
        print("sua média é {}, voce foi provado com distinção.".format(media))
    elif media >=7.0 and media != 10.0:
        print("sua média é {}, voce foi Aprovado.".format(media))
    else:
        print("sua média é {}, voce foi Reprovado.".format(media))
else:
    print("é impossivel a média ser maior que 10!")