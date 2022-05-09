#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
arquivo = float(input("Digite o Tamanho do arquivo em MB: "))
vel_net = float(input("Digite a Velocidade de Internet em MBps: "))
print("Tempo de download: %.0f Minutos " %(60 * (arquivo / vel_net)))