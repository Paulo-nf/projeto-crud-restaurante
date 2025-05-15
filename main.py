import CRUD_Exemplo as exemplo
import os
import terminal_bonito


def menu_inicial():
    terminal_bonito.limpar_terminal()
    terminal_bonito.linha_horizontal()
    terminal_bonito.print_bonito("BEM VINDO AO SISTEMA RESTAURANTE SOLUTIONS™")
    terminal_bonito.print_bonito("""
    1 - MÓDULO MESAS
    2 - MÓDULO PRATOS
    3 - MÓDULO PEDIDOS
    4 - MÓDULO EXEMPLO
    5 - SAIR
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
                # aqui vai ser crud de mesas
                pass
            case 2:
                # aqui vai ser crud de pratos
                pass
            case 3:
                # aqui var ser crud de pedidos
                pass
            case 4:
                while True:
                    terminal_bonito.limpar_terminal()
                    terminal_bonito.linha_horizontal()
                    exemplo.menu()
                    terminal_bonito.linha_horizontal()
                    opcao = terminal_bonito.input_bonito("INFORME SUA OPÇÃO: ")

                    if opcao == "1":
                        nome = input("DIGITE O NOME: ")
                        idade = input("DIGITE A IDADE: ")
                        exemplo.adicionar_usuario(nome, idade)
                    elif opcao == "2":
                        exemplo.listar_usuarios()
                        input("Aperte enter para continuar...")
                    elif opcao == "3":
                        nome_antigo = input("DIGITE O NOME A SER ATUALIZADO: ")
                        novo_nome = input("DIGITE O NOVO NOME: ")
                        nova_idade = input("DIGITE A NOVA IDADE: ")
                        exemplo.atualizar_usuario(nome_antigo, novo_nome, nova_idade)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO: ")
                        exemplo.excluir_usuario(nome)
                    elif opcao == "5":
                        nome = input("DIGITE O NOME DO USUÁRIO: ")
                        exemplo.buscar_usuario(nome)
                        input("Aperte enter para continuar...")
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        break
                    else:
                        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 5:
                print("SAINDO...")
                break
            case __:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main()
