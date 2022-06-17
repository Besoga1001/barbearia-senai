from cadastro_cliente import cadastro, valida_cadastro

def login(nome_cadastro2, senha_cadastro2):
    global login_nome
    global login_senha
    existe_cadastro = 0
    print('Login do Cliente.\nEntre com suas informações! ')
    login_nome = input('Nome: ')
    login_senha = input('Senha: ')
    valida_cadastro(login_nome, login_senha, nome_cadastro2, senha_cadastro2)
    if existe_cadastro == 1:
        print('Login efeituado com sucesso.')
    else:
        print('Login não cadastrado.')
        tela_cliente()

def tela_cliente():
    tela = 0
    while (tela != 1) or (tela != 2):
        print('\nVocê já tem cadastro?\n'
              '1 - Tela de Login\n'
              '2 - Tela de Cadastro')

        tela = int(input('Digite o número da opção desejada: '))

        if tela == 1:
            login(nome_cadastro2, senha_cadastro2)
        elif tela == 2:
            cadastro()
            from cadastro_cliente import nome_cadastro, senha_cadastro
            nome_cadastro2 = nome_cadastro
            senha_cadastro2 = senha_cadastro