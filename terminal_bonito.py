import os

class Cor:
    AZUL = '\033[94m'
    CIANO = '\033[96m'
    RESET = '\033[0m' # reseta Cor no terminal

def linha_horizontal():
    print(Cor.CIANO + "=" * 55 + Cor.RESET)

def print_bonito(texto):
    print(Cor.AZUL + texto + Cor.RESET)

def input_bonito(texto):
    return input(Cor.AZUL + texto + Cor.RESET)

def limpar_terminal():
    # os.system permite escreve comandos pro terminal
    # os.name == 'nt' indica que o sistema operacional é Windows
    # o comando 'cls' limpa o terminal no windows
    # o comando 'clear' limpa o terminal no linux/macOS
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
