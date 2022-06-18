listaCadastroCliente = []


def receberDadosCadastro():
    print('Cadastro Cliente\nEntre com suas informações: ')
    nome_cadastro = str(input('Nome: '))
    senha_cadastro = str(input('Senha: '))
    confirmar_senha_cadastro = str(input('Confirmar Senha: '))

    while senha_cadastro != confirmar_senha_cadastro:
        print('Senha não é igual, digite novamente!.')
        senha_cadastro = str(input('Senha: '))
        confirmar_senha_cadastro = str(input('Confirmar Senha: '))

    print('Cadastro concluído com sucesso.')
    return [nome_cadastro, senha_cadastro]


def inserirCadastro(listaCadastroCliente):
    dadosCadastro = receberDadosCadastro()
    listaCadastroCliente.append(dadosCadastro)


def valida_cadastro(valida_nome, valida_senha, listaCadastro):
    for l in range(0, 2):
        if (valida_nome == listaCadastroCliente[l][0]) and (valida_senha == listaCadastroCliente[l][1]):
            return 1


def login(listaCadastroCliente):
    global login_nome
    global login_senha

    print('\nLogin do Cliente.\nEntre com suas informações! ')
    login_nome = input('Nome: ')
    login_senha = input('Senha: ')

    try:
        existe_cadastro = valida_cadastro(login_nome, login_senha, listaCadastroCliente)
        if existe_cadastro == 1:
            print('Login de cliente efeituado com sucesso.')
            from completo import selecionaCorte, selecionaBarbeiro, mostraHorariosFuncionamento

            selecionaCorte()
            selecionaBarbeiro()
            mostraHorariosFuncionamento()
        else:
            print('Login não cadastrado.')
            tela_cliente()
    except:
        print('Login não cadastrado.')
        tela_cliente()


def tela_cliente():
    tela = ''
    while (tela != '1') or (tela != '2'):

        print('\nTela de Cliente\n'
              '1 - Tela de Login\n'
              '2 - Tela de Cadastro')

        tela = str(input('Digite o número da opção desejada: '))

        if tela == '1':
            login(listaCadastroCliente)
        elif tela == '2':
            inserirCadastro(listaCadastroCliente)
