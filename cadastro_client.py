print('Cadastro Cliente\nEntre com suas informações: ')
user_name_cadastro = input(str('Username: '))
senha_cadastro = input(str('Senha: '))
confirmar_senha_cadastro = input(str('Confirmar Senha: '))

if (senha_cadastro == confirmar_senha_cadastro):
    validar_cadastro = 1
else:
    validar_cadastro = 0

