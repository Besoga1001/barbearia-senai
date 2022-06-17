nome_cadastro = ''
cpf_cadastro = 0
senha_cadastro = ''
confirmar_senha_cadastro = ''

def cadastro():

    print('Cadastro Cliente\nEntre com suas informações: ')
    nome_cadastro = input('Nome: ')
    senha_cadastro = input('Senha: ')
    confirmar_senha_cadastro = input('Confirmar Senha: ')

    while senha_cadastro != confirmar_senha_cadastro:
        print('Senha não é igual, digite novamente!.')
        senha_cadastro = input('Senha: ')
        confirmar_senha_cadastro = input('Confirmar Senha: ')

    print('Cadastro concluído com sucesso.')
    print(nome_cadastro, senha_cadastro)


def valida_cadastro(valida_nome, valida_senha, nome_cadastro, senha_cadastro):
    if (valida_nome == nome_cadastro) and (valida_senha == senha_cadastro):
        return 1
    else:
        return 0