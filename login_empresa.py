listaCadastro = []


def receberDadosCadastro():
    print('\nCadastro Empresa\nEntre com suas informações')
    nome_cadastro = str(input('Nome: '))
    senha_cadastro = str(input('Senha: '))
    confirmar_senha_cadastro = str(input('Confirmar Senha: '))

    while senha_cadastro != confirmar_senha_cadastro:
        print('Senha não é igual, digite novamente!.')
        senha_cadastro = str(input('Senha: '))
        confirmar_senha_cadastro = str(input('Confirmar Senha: '))

    print('Cadastro concluído com sucesso.')
    return [nome_cadastro, senha_cadastro]


def inserirCadastro(listaCadastro):
    dadosCadastro = receberDadosCadastro()
    listaCadastro.append(dadosCadastro)
    tela_empresa()


def valida_cadastro(valida_nome, valida_senha, listaCadastro):

    for l in range(0,2):
        if (valida_nome == listaCadastro[l][0]) and (valida_senha == listaCadastro[l][1]):
            return 1


def login(listaCadastro):
    global login_nome
    global login_senha

    print('\nLogin da Empresa.\nEntre com suas informações! ')
    login_nome = input('Nome: ')
    login_senha = input('Senha: ')

    #try:
    existe_cadastro = valida_cadastro(login_nome, login_senha, listaCadastro)
    if existe_cadastro == 1:
        print('Login de empresa efeituado com sucesso.')
        from consultar_agenda import escolheConsulta

        escolheConsulta()
    else:
        print('Login não cadastrado.')
        tela_empresa()
    #except:
        #print('Login não cadastrado.')
        #tela_empresa()


def tela_empresa():
    #try:
    print('\nTela de Empresa\n'
          '1 - Tela de Login\n'
          '2 - Tela de Cadastro')

    tela = str(input('Digite o número da opção desejada: '))

    if tela == '1':
        login(listaCadastro)
    elif tela == '2':
        inserirCadastro(listaCadastro)
    #except:
        #print('Opção Inválida, favor digitar novamente.')
        #tela_empresa()