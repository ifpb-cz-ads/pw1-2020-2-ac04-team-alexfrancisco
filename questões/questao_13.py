
numero = 'true'
soma,media = 0,0
cont = 0

while(numero != 0):
    numero = int(input("Type the number: "))
    soma += numero
    cont+=1

media = soma/cont
print(" Quantidade de numeros digitados: %d\n Soma: %d\n Média Aritmética: %.1f" %(cont,soma,media))
    
