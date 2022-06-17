from sys import exit
from os import name, system

users = {}
status = ''

def clear():
    if name == 'nt':
        _ = system('cls')
def newUser():
    newUsername = input('Digite o nome de sua empresa: ')

    if newUsername in users:
        print('\nEste ID empresarial já existe!\n')
        input('Pressione [Enter] para continuar')
    else:
        newPassword = input('Crie uma nova senha: ')
        users[newUsername] = newPassword
        print('\nID de empresa criada com Sucesso!\n')
        input('Pressione [Enter] para continuar')

def oldUser():
    login = input('insira o nome de sua empresa: ')
    password = input('insira sua senha: ')
    if login in users and users[login] == password:
        print('\nLogin feito!\n')
        input('Pressiona [Enter] para continuar')
    else:
        print('\nLogin incorreto!\n')
        input('Pressione [Enter] para continuar')

while True:
    clear()
    status = input('Você é dono de uma empresa registrada? [s/n] Digite [sair] para sair\n> ')
    status = status.lower()
    if status == 's':
        oldUser()
    elif status == 'n':
        newUser()
    elif status == 'sair':
        exit()
    else:
        continue