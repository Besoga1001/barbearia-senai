def cadastro():
    print('Cadastro Cliente\nEntre com suas informações: ')
    nome_cadastro = input('Nome: ')
    cpf_cadastro = int(input('Cpf: '))
    senha_cadastro = input('Senha: ')
    confirmar_senha_cadastro = input('Confirmar Senha: ')

    while senha_cadastro != confirmar_senha_cadastro:
        print('Senha não é igual, digite novamente!.')
        senha_cadastro = input('Senha: ')
        confirmar_senha_cadastro = input('Confirmar Senha: ')

    print('Cadastro concluído com sucesso.')