tela1 = 1

print('Bem-vindo ao aplicativo de agendamento da Barbearia X')

while (tela1 == 1):
    tipoUsuario = int(input('Você é cliente ou empresa? \nDigite 1 para cliente ou 2 para empresa: '))

    if (tipoUsuario == 1):
        tela1 = 0
        from login_cliente import tela_cliente
        tela_cliente()
    elif(tipoUsuario == 2):
        tela1 = 0
        from login_empresa import tela_cadastro
        tela_cadastro()
    else:
        print('Opção Inválida, favor digitar novamente.')
        tela1 = 1