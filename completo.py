#jo.987victor@gmail.com
atividade = int(input('Atividade desejada: '))
if atividade == 1:
    print('O que você deseja fazer?\n'
        '1- Cortar o cabelo\n'
        '2- Fazer a Barba\n'
        '3- Fazer a Sombrancelha\n'
        '4- Fazer Completo\n')
    Resposta = int(input('Digite o numero Desejado: '))
    if Resposta == 1:
        print ('Você reservou um Corte de Cabelo')
    elif Resposta == 2:
        print ('Você reservou para Fazer a Barba')
    elif Resposta == 3:
        print ('Você reservou para Fazer Sombrancelha')
    elif Resposta == 4:
        print ('Você reservou um Corte Completo')
    else:
        print('Digite Novamente ')

if atividade == 2:
    print('Com qual Barbeiro você deseja Fazer o Serviço?\n'
    '1- Barbeiro 1\n'
    '2- Barbeiro 2\n'
    '3- Barbeiro 3\n'
    '4- Barbeiro 4\n')
    Resposta = int(input('Digite o numero do Barbeiro Desejado: '))
    if Resposta == 1:
        print ('Barbeiro 1 Escolhido com sucesso')
    elif Resposta == 2:
        print ('Barbeiro 2 Escolhido com sucesso')
    elif Resposta == 3:
        print ('Barbeiro 3 Escolhido com sucesso')
    elif Resposta == 4:
        print ('Barbeiro 4 Escolhido com sucesso')
    else:
        print('Digite Novamente')
        
if atividade == 3:
    horarios = print('Esses são os horarios de Funcionamento de Segunda a Sexta:\n'
    '08:00\n'
    '09:00\n'
    '10:00\n'
    '11:00\n'
    '13:00\n'
    '14:00\n'
    '14:00\n'
    '15:00\n'
    '16:00\n'
    '17:00\n'
    '18:00\n')
    print('Os Horarios de Funcionamento da {}'.format(horarios))