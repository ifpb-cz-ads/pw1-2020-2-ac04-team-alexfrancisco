
print(" Menu\n [1] Adição\n [2] Subtração\n [3] Multiplicação\n [4] Divisão\n [5] Sair\n")

num = int(input("Informe a operação escolhida:"))
cont = 1

while(num != 5):
    #print(" Menu\n [1] Adição\n [2] Subtração\n [3] Multiplicação\n [4] Divisão\n [5] Sair\n")
    if num == 1:
        entrada = int(input("Digite o valor da tabuada que deseja:"))
        while(cont <= 10):
            print("%d + %d = %d" %(entrada, cont, entrada+cont))
            cont+=1
        cont = 1

    elif num == 2:
        entrada = int(input("Digite o valor da tabuada que deseja:"))
        while(cont <= 10):
            print("%d - %d = %d" %(entrada, cont, entrada-cont))
            cont+=1
        cont = 1
    elif num == 3:
        entrada = int(input("Digite o valor da tabuada que deseja:"))
        while(cont <= 10):
            print("%d * %d = %d" %(entrada, cont, entrada*cont))
            cont+=1
        cont = 1
    elif num == 4:
        entrada = int(input("Digite o valor da tabuada que deseja:"))
        while(cont <= 10):
            print("%d / %d = %.1f" %(entrada, cont, entrada/cont))
            cont+=1
        cont = 1
    num = int(input("Informe a operação escolhida:"))
