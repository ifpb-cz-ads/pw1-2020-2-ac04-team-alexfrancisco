n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
resto = n1 - n2
divisao = 1

while resto >= n2:
    resto -= n2
    divisao += 1

print('Resultado da divisão %d / %d = %d' %(n1, n2, divisao))
print('Resto da divisão = %d' %resto)
