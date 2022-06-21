#jo.987victor@gmail.com
quadro_segunda = [
    ['Segunda'],
    ['08:00'],
    ['09:00'],
    ['10:00']
]

quadro_terca = [
    ['Terça'],
    ['08:00'],
    ['09:00'],
    ['10:00']
]

quadro_quarta = [
    ['Quarta'],
    ['08:00'],
    ['09:00'],
    ['10:00']
]

quadro_quinta = [
    ['Quinta'],
    ['08:00'],
    ['09:00'],
    ['10:00']
]

quadro_sexta = [
    ['Sexta'],
    ['15:00'],
    ['16:00'],
    ['17:00']
]

x = '11:00'

registro = [
    ['Nome', 'Tipo', 'Barbeiro', 'Dia da Semana', 'Horarios'],
    ['Bernardo', 'Completo', 'Barbeiro 1', 'Segunda', '14:00']
]

registro_linha = []

def selecionaCorte():
    print('O que você deseja fazer?\n'
        '1- Cortar o cabelo\n'
        '2- Fazer a Barba\n'
        '3- Fazer a Sombrancelha\n'
        '4- Fazer Completo\n')
    resposta = int(input('Digite o número da opção desejada: '))

    if resposta == 1:
        print ('Você reservou um Corte de Cabelo')
        registro_linha.append('Cabelo')
    elif resposta == 2:
        print ('Você reservou para Fazer a Barba')
        registro_linha.append('Barba')
    elif resposta == 3:
        print ('Você reservou para Fazer Sombrancelha')
        registro_linha.append('Sombrancelha')
    elif resposta == 4:
        print ('Você reservou um Corte Completo')
        registro_linha.append('Completo')
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
        registro_linha.append('Barbeiro 1')
    elif resposta == 2:
        print ('Barbeiro 2 Escolhido com sucesso\n')
        registro_linha.append('Barbeiro 2')
    elif resposta == 3:
        print ('Barbeiro 3 Escolhido com sucesso\n')
        registro_linha.append('Barbeiro 3')
    elif resposta == 4:
        print ('Barbeiro 4 Escolhido com sucesso\n')
        registro_linha.append('Barbeiro 4')
    else:
        print('Digite Novamente')


def escolheDiaSemana():

    resposta = ''

    print('Qual dia da semana você deseja?\n'
    '1- Segunda\n'
    '2- Terça\n'
    '3- Quarta\n'
    '4- Quinta\n'
    '5- Sexta\n')

    resposta = int(input('Digite o número da opção desejada: '))
    if resposta == 1:
        print ('Segunda Escolhida com sucesso\n')
        registro_linha.append('Segunda')
    elif resposta == 2:
        print ('Terça Escolhida com sucesso\n')
        registro_linha.append('Terça')
    elif resposta == 3:
        print ('Quarta Escolhida com sucesso\n')
        registro_linha.append('Quarta')
    elif resposta == 4:
        print ('Quinta Escolhida com sucesso\n')
        registro_linha.append('Quinta')
    elif resposta == 5:
        print ('Sexta Escolhida com sucesso\n')
        registro_linha.append('Sexta')
    else:
        print('Digite Novamente')


def selecionarHorario():
    try:
        horario = input('\nSelecione o horário para o concluir o agendamento: ')
        return horario
    except:
        print('\nHorário não disponivel, selecione novamente')
        selecionarHorario()


def mostraHorariosFuncionamento():
    dia = registro_linha[3]
    print('Esses são os horários disponíveis de',dia+':\n')
    if dia == 'Segunda':
        for x in range(0,4):
            print(quadro_segunda[x][0])
        h = selecionarHorario()
        for x in range(0, 4):
            if h in quadro_segunda:
                quadro_segunda[x][0] = ''
                print(quadro_segunda[x][0])
    elif dia == 'Terça':
        for x in range(0,4):
            print(quadro_terca[x][0])
    elif dia == 'Quarta':
        for x in range(0,4):
            print(quadro_quarta[x][0])
    elif dia == 'Quinta':
        for x in range(0,4):
            print(quadro_quinta[x][0])
    else:
        for x in range(0,4):
            print(quadro_sexta[x][0])


