import leia
from ex115.lib.arquivo import *
arq = 'usuarios.txt'
if not arqExist(arq):
    criarArq(arq)
while True:
    op = menu(['Ver usuários cadastrados', 'Cadastrar novo usuário', 'Sair'])
    if op == 1:
        titulo('USUÁRIOS CADASTRADOS')
        lerArq(arq)
    elif op == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title()
        if nome is '':
            nome = str('Usuário Desconhecido')
        idade = leia.leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif op == 3:
        titulo('ENCERRANDO...')
        break
