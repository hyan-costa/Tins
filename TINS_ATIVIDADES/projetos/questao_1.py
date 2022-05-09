import os
#funcao que converte byte para mb
def byte_mb(quantidade):
    #arredenoda os bytes para 2 casas, substitui a . por ,
    return str(round(quantidade/1048576,2)).replace('.',',')

def porcentagem(usado,total):
    return str(round((usado*100)/total,2)).replace('.',',')

#analisa se o arquivo existe
if os.path.exists("usuarios.txt"):
    usuarios_txt = open("usuarios.txt","r")
    usuarios_espacos = usuarios_txt.read().split("\n")
    #analisa se os espaços são maior que 0
    if len(usuarios_espacos) >=1:
        arquivo_rel = open("relatorio.txt","w")
        arquivo_rel.write("ACME Inc.           Uso do espaco em disco pelos usuarios\n")
        arquivo_rel.write("------------------------------------------------------------------------\n")
        arquivo_rel.write("Nr".ljust(5))
        arquivo_rel.write("Usuario".ljust(15))
        arquivo_rel.write("Espaco utilizado".ljust(15))
        arquivo_rel.write("% do uso".ljust(9) + "\n\n")
        
        espaco_Total = 0
        for usuario_espaco in usuarios_espacos:
            espaco_Total += int(usuario_espaco.split()[1])
        
        for cont in range(len(usuarios_espacos)):
            usuario_espaco = usuarios_espacos[cont].split()
        
            usuario = usuario_espaco[0]
            espaco = usuario_espaco[1]
            #adiciona os usuarios e os mb's no arquivo
            arquivo_rel.write(str(cont+1).ljust(5))
            arquivo_rel.write(usuario.ljust(15))
            arquivo_rel.write(byte_mb(int(espaco)).rjust(7)+" MB".rjust(12))
            arquivo_rel.write(porcentagem(int(espaco),espaco_Total).rjust(7)+"%\n")
        
        arquivo_rel.write("\nespaco total ocupado:"+ byte_mb(espaco_Total)+" MB\n")
        arquivo_rel.write("espaco medio ocupado"+ byte_mb(espaco_Total/len(usuarios_espacos))+ " MB")
        arquivo_rel.close()
        
        
        
else:
    print("arquivo nao encontrado!")