import random

def embaralhar(s):
    embaralha = random.sample(s, len(s)) 
    a = ''.join(embaralha) 
    print (a)

palavra = input("digite uma palavra: ")
embaralhar(palavra)