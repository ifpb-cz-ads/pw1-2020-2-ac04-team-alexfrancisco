codigo = int(input('Informe o código do produto: '))
total = 0

while codigo != 0:

    quantidade = int(input('Informe a quantidade adquirida do produto: '))

    if codigo == 1:
        total += (quantidade * 0.5)
    elif codigo == 2:
        total += (quantidade * 1)
    elif codigo == 3:
        total += (quantidade * 4)
    elif codigo == 5:
        total += (quantidade * 7)
    elif codigo == 9:
        total += (quantidade * 8)
    else:
        print('Código inválido.')

    print('Total: R$ %.2f' %(total))
    codigo = int(input('Informe o código do produto: '))

print('Total: R$ %.2f' %(total))