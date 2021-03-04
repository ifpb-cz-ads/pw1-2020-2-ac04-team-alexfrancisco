import math

dividaInicial = float(input('Informe o valor inicial da dívida: '))
juroMensal = float(input('Informe o juro mensal: '))
valorPagoPorMes = float(input('Informe o valor que será pago por mês: '))
totalMeses = math.ceil(dividaInicial / valorPagoPorMes)
totalJuros = (juroMensal * totalMeses)
totalAPagar = (dividaInicial + totalJuros)

print('Serão necessários %d meses para pagar a dívida' %(totalMeses))
print('Você irá pagar R$ %.2f' %(totalAPagar))
print('R$ %.2f são juros mensais' %(totalJuros))