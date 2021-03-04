valorInicial = float(input('Informe o valor inicial do depósito: '))
juros = float(input('Informe a taxa de juros da poupança: '))
ganhos = 0
atual = valorInicial
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for c in meses:
    atual = atual + (atual * juros)
    print('Em %s o saldo da conta estava em R$ %.2f' %(c, atual))

print('Os ganhos foram de R$ %.2f' %(atual - valorInicial))