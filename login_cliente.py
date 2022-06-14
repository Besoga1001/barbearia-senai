tela = ''
def tela_cliente():
    global tela
    while (tela != 'C') or (tela != 'L'):
        tela = input('Digite C para acessar tela de cadastro ou digite L para acessar tela de login: ')

        if tela == 'C':
            from cadastro_cliente import cadastro
            cadastro()
        elif tela == 'L':
            print('Login do Cliente.\nEntre com suas informações! ')