n = int(input('Tabuada de: '))
inicio = int(input("Início da tabuada: "))
fim = int(input('Fim da tabuada: '))

if inicio > fim:
    print('Informe um valor de início menor que o valor de fim.')
else:
    while inicio <= fim:
        print('%d x %d = %d' %(inicio, n, (inicio * n)))
        inicio += 1
