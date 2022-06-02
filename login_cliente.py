tela1 = ''

while (tela1 != 'C' or tela1 != 'L'):
    tela1 = input(str('Digite C para acessar tela de cadastro ou digite L para acessar tela de login: '))

    if (tela1 == 'C'):
        import cadastro_client
    elif (tela1 == 'L'):
        print('Login do Cliente.\nEntre com suas informações: ')


