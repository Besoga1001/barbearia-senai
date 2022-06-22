quadro_horario = [
    ['Segunda', '08:00', '09:00', '10:00'],
    ['Terça', '08:00', '09:00', '10:00'],
    ['Quarta', '08:00', '09:00', '10:00'],
    ['Quinta', '08:00', '09:00', '10:00'],
    ['Sexta', '08:00', '09:00', '10:00'],
]

registro = [
    ['Nome', 'Tipo', 'Barbeiro', 'Dia', 'Horário']
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
    #try:
    horario = str(input('\nSelecione o horário para o concluir o agendamento: '))
    return horario
    #except:
        #print('\nHorário não disponivel, selecione novamente.')
        #selecionarHorario()


def alteraMatriz(x):
    for y in range(4):
        print(quadro_horario[x][y])
    h = selecionarHorario()
    for y in range(4):
        if h == quadro_horario[x][y]:
            quadro_horario[x][y] = ''
            registro_linha.append(h)
            break


def mostraHorariosFuncionamento():
    dia = registro_linha[3]
    print('Esses são os horários disponíveis de',dia+':\n')

    if dia == 'Segunda':
        x = 0
        alteraMatriz(x)
    elif dia == 'Terça':
        x = 1
        alteraMatriz(x)
    elif dia == 'Quarta':
        x = 2
        alteraMatriz(x)
    elif dia == 'Quinta':
        x = 3
        alteraMatriz(x)
    elif dia == 'Sexta':
        x = 4
        alteraMatriz(x)

    registro.append(registro_linha)
    print(registro)
    print('Agendamento concluído com sucesso\n')
    from main import inicio

    inicio()