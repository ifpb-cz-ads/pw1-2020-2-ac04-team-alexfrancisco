n1 = int(input('Informe um número inteiro: '))

if n1 == 0 or n1 == 1:
    print('Não é um número primo.')
elif n1 == 2:
    print('É um número primo.')
else:
    resto = (n1 % 2)
    if resto == 0:
        print('Não é um número primo.')
    else:
        c = 1
        ehPrimo = True
        while c <= n1:
            if (c / 2) == 0:
                ehPrimo = False
            c += 2

        if ehPrimo:
            print('%d é um número primo' %(n1))
        else:
            print('%d não é um número primo' %(n1))