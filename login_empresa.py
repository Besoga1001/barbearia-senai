print('Login Empresa!')

tela = ''

def tela_empresa():
    global tela_empresa
    while (tela_empresa != '1') or (tela_empresa != '2'):
        tela_empresa = input('Digite 1 para acessar tela de cadastro ou digite 2 para acessar tela de login: ')

        if tela_empresa == '1':
            from cadastro_empresa import cadastro_empresa
            cadastro_empresa()
        elif tela_empresa == '2':
            print('Login da Empresa.\nEntre com suas informações!')