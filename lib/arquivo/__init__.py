from ex115.lib.interface import *


def arqExist(arq):  # Função que valida se o arquivo de usuários existe ou não
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(arq):  # Função que cria um arquivo de texto para cadastrar os usuários (caso ele não exista)
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except:
        print(f'{colors.vermelho()}ERRO: Criação do arquivo!{colors.limpa()}')
    else:
        print(f'{colors.verde()}Arquivo {arq} criado com sucesso!{colors.limpa()}')


def lerArq(arq):  # Função que lê o arquivo de texto dos usuários cadastrados
    try:
        arquivo = open(arq, 'rt')
    except:
        print(f'{colors.vermelho()}ERRO: Leitura do arquivo!{colors.limpa()}')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')


def cadastro(arq, nome, idade=0):  # Função de cadastro de nome e idade dos usuários
    try:
        arquivo = open(arq, 'at')
    except:
        print(f'{colors.vermelho()}ERRO: Abertura do arquivo!{colors.limpa()}')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print(f'{colors.vermelho()}ERRO: Dados não foram salvos no arquivo!{colors.limpa()}')
        else:
            print(f'{colors.verde()}Usuário {nome} cadastrado com sucesso!{colors.limpa()}')
            arquivo.close()
