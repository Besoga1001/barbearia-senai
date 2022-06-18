print('Bem-vindo ao aplicativo de agendamento da Barbearia X')

def inicio():
    while True:
        print('Você é cliente ou empresa? \n'
        '1 - Cliente\n'
        '2 - Empresa')

        tipoUsuario = input('Digite o número da opção desejada: ')

        if tipoUsuario == '1':
            from login_cliente import tela_cliente

            tela_cliente()
            break
        elif tipoUsuario == '2':
            from login_empresa import tela_empresa

            tela_empresa()
            break
        else:
            print('Opção Inválida, favor digitar novamente.')
            continue

inicio()