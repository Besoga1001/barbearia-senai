tela1 = 1

print('Bem-vindo ao aplicativo de agendamento da Barbearia X')

while tela1 == 1:
    print('Você é cliente ou empresa? \n'
    '1 - Cliente\n'
    '2 - Empresa')

    tipoUsuario = int(input('Digite o número da opção desejada: '))

    if tipoUsuario == 1:
        tela1 = 0
        from login_cliente import tela_cliente

        tela_cliente()
    elif tipoUsuario == 2:
        tela1 = 0
    #       from login_empresa import tela_cadastro

    #       tela_cadastro()
    else:
        print('Opção Inválida, favor digitar novamente.')
        tela1 = 1