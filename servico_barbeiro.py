#Parte empresa:
numero = int(input('Digite quantos serviços disponiveis a sua empresa tem: '))
if numero == 0 or numero < 10:
    print('Digite Novamente')
    

if numero == 1:
    input('1: ')
n=0
while n > 0:
    if numero > 1:
        input('2: ', * numero)
