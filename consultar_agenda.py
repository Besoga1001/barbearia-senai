from completo import registro, quadro_horario

def consultaHorarios():
    for x in range(5):
        for y in range(4):
            print(quadro_horario[x][y], end=' ')
            if y == 3:
                print('')


def consultaAgenda():
    n = len(registro)

    for x in range(0, n):
        print(x)
        for y in range(0, 5):
            print(registro[x][y], end=' ')
            if y == 4:
                print('')


def escolheConsulta():
    print('\nConsulta da Empresa\n'
          '1 - Consultar Horários Disponíveis\n'
          '2 - Consultar Agendamentos\n'
          '3 - Retornar para Tela Inicial')

    tipoConsulta = input('Digite o número da opção desejada: ')

    if tipoConsulta == '1':
        print('')
        consultaHorarios()
        escolheConsulta()
    elif tipoConsulta == '2':
        print('')

        consultaAgenda()
        escolheConsulta()
    elif tipoConsulta == '3':
        from main import inicio

        inicio()
    else:
        print('Opção Inválida, favor digitar novamente.')
        escolheConsulta()
