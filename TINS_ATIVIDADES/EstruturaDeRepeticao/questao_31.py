# Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
# indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro
# que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, 
# o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

while 1:
    cont = 0
    val_total = 0
    while 1:
        cont+=1
        produto = float(input("produto {}:".format(cont)))
        val_total +=produto
    
        if produto ==0:
            print("-------------------------------------")
            print("total: R$ %.2f"% val_total)
            print("press. ctrl + c para sair ou continue")
            print("-------------------------------------")
            cont = 0
            val_total = 0
                