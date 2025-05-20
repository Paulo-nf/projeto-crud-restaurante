import os
import terminal_bonito
import crud_mesas as mesas
import crud_pratos as pratos
import crud_pedidos as pedidos


def menu_inicial():
    terminal_bonito.limpar_terminal()
    terminal_bonito.linha_horizontal()
    terminal_bonito.print_bonito("BEM VINDO AO SISTEMA RESTAURANTE SOLUTIONS™")
    terminal_bonito.print_bonito("""
    1 - MÓDULO MESAS
    2 - MÓDULO PRATOS
    3 - MÓDULO PEDIDOS
    4 - SAIR
    """)

def main():

    while True:
        terminal_bonito.limpar_terminal()
        menu_inicial()
        terminal_bonito.linha_horizontal()
        opcao_inicial = int(terminal_bonito.input_bonito("INFORME SUA OPÇÃO: "))
        terminal_bonito.limpar_terminal()

        terminal_bonito.linha_horizontal()

        match opcao_inicial:
            case 1:
                mesas.menu()
                pass
            case 2:
                pratos.menu()
            case 3:
                pedidos.menu_pedidos()
            case 4:
                print("SAINDO...")
                break
            case __:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main()
