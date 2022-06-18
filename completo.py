#jo.987victor@gmail.com

quadro_horarios = [
    ['Segunda'] , ['Terça']   , ['Quarta']    , ['Quinta'] , ['Sexta'],
    ['08:00']   , ['08:00']   , ['08:00']     , ['08:00']  , ['08:00'],
    ['09:00']   , ['09:00']   , ['09:00']     , ['09:00']  , ['09:00'],
    ['10:00']   , ['10:00']   , ['10:00']     , ['10:00']  , ['10:00'],
    ['11:00']   , ['11:00']   , ['11:00']     , ['11:00']  , ['11:00'],
    ['13:00']   , ['13:00']   , ['13:00']     , ['13:00']  , ['13:00'],
    ['14:00']   , ['14:00']   , ['14:00']     , ['14:00']  , ['14:00'],
    ['15:00']   , ['15:00']   , ['15:00']     , ['15:00']  , ['15:00'],
    ['16:00']   , ['16:00']   , ['16:00']     , ['16:00']  , ['16:00'],
    ['17:00']   , ['17:00']   , ['17:00']     , ['17:00']  , ['17:00'],
    ['18:00']   , ['18:00']   , ['18:00']     , ['18:00']  , ['18:00'],
            ]

registro = [
    ['Nome']    , ['Tipo']    , ['Barbeiro']  , ['Dia da Semana'], ['Horário']
    ['Bernardo'], ['Completo'], ['Barbeiro 2'], ['Segunda']      , ['14:00']
            ]

def selecionaCorte():
    print('O que você deseja fazer?\n'
        '1- Cortar o cabelo\n'
        '2- Fazer a Barba\n'
        '3- Fazer a Sombrancelha\n'
        '4- Fazer Completo\n')
    resposta = int(input('Digite o número da opção desejada: '))

    if resposta == 1:
        print ('Você reservou um Corte de Cabelo')
    elif resposta == 2:
        print ('Você reservou para Fazer a Barba')
    elif resposta == 3:
        print ('Você reservou para Fazer Sombrancelha')
    elif resposta == 4:
        print ('Você reservou um Corte Completo')
    else:
        print('Digite Novamente ')


def selecionaBarbeiro():
    resposta = ''

    print('Com qual Barbeiro você deseja Fazer o Serviço?\n'
    '1- Barbeiro 1\n'
    '2- Barbeiro 2\n'
    '3- Barbeiro 3\n'
    '4- Barbeiro 4\n')

    resposta = int(input('Digite o numero do Barbeiro Desejado: '))
    if resposta == 1:
        print ('Barbeiro 1 Escolhido com sucesso\n')
    elif resposta == 2:
        print ('Barbeiro 2 Escolhido com sucesso\n')
    elif resposta == 3:
        print ('Barbeiro 3 Escolhido com sucesso\n')
    elif resposta == 4:
        print ('Barbeiro 4 Escolhido com sucesso\n')
    else:
        print('Digite Novamente')


def mostraHorariosFuncionamento():
    print('Esses são os horarios de Funcionamento de Segunda a Sexta:\n'
    '08:00\n'
    '09:00\n'
    '10:00\n'
    '11:00\n'
    '13:00\n'
    '14:00\n'
    '15:00\n'
    '16:00\n'
    '17:00\n'
    '18:00\n')
    print('Os Horarios de Funcionamento da Barbearia X')

