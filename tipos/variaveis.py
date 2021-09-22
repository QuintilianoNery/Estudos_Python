from typing import TextIO


a = 3

b = 4.4

print(a+b)


texto = 'sua idade ...'

idade = 23

#não é a melhor forma de se fazer convertendo para string
#print(texto + str(idade))
print(f'{texto} {idade}')

saudacao = ' bom dia '
print(3 * saudacao)

PI = 3.14

raio = float (input ('informe o raio da circunferencia?'))

#area = PI * raio *raio
#em poténcia
area = PI * pow(raio, 2)
print(f'A Área da circunferência é {area}m2')



