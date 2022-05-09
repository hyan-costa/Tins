import random


#busca as palavras do arquivo.txt
consulta = open("arquivo.txt",'r')
palavras = consulta.readlines()
consulta.close()

#funçao para escrever a palavra
def print_forca(forca):
    print(' '.join(forca).upper())
    print('')
	
palavra = random.choice(palavras)
#escreve a quantidade de _ igual ao numero de palavras. o -1 é para diminuir uma casa
forca = ['_' for i in range(len(palavra)-1)]
erros = 0
ganhou = False

#caso o usuario erre pela de 6 veze e e voce tenha perdido, o programa para
while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra:')
    chute = str(input()).lower()

    if chute not in palavra:
        erros += 1
        print(f'Você errou pela {erros}° vez.')
        continue
        #adiciona a letra correta na palavra
    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute

    if '_' not in forca:
        ganhou = True

if ganhou:
    print('You win!')
else:
    print('Game over!')
print_forca(forca)
