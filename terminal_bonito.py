import os

class Cor:
    AZUL = '\033[94m'
    LINHA = '\033[96m'
    RESET = '\033[0m' # reseta Cor no terminal

def linha_horizontal():
    print(Cor.LINHA + "=" * 55 + Cor.RESET)

def print_bonito(texto):
    print(Cor.AZUL + texto + Cor.RESET)

def input_bonito(texto):
    return input(Cor.AZUL + texto + Cor.RESET)

def limpar_terminal():
    # os.name == 'nt' indica que o sistema operacional é Windows
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
