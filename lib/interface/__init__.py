import colors  # Importa a biblioteca colors criada por mim para colocar cores no menu


def lin(tam=50):  # Função de criar linhas de divisão quando chamadas
    return '-'*tam


def titulo(txt):  # Função de criar um cabeçalho/título
    print(lin())
    print(f'{txt:^50}')
    print(lin())


def menu(opcoes):  # Função do menu com as opções onde o utilizador escolhe o que será executado no programa
    from leia import leiaInt
    titulo('MENU PRINCIPAL')
    c = 1
    for i in opcoes:
        print(f'{colors.amarelo_c()}{c}{colors.limpa()} - {colors.azul()}{i}{colors.limpa()}')
        c += 1
    print(lin())
    op = leiaInt(f'{colors.magenta()}Opção: {colors.limpa()}')
    while op != 1 and op != 2 and op != 3:
        print(f'{colors.vermelho()}ERRO: Digite uma opção válida!{colors.limpa()}')
        op = leiaInt(f'{colors.magenta()}Opção: {colors.limpa()}')
    else:
        return op
