import CRUD_Exemplo as exemplo
import os
from cor import Cor

def linha_horizontal():
    print(Cor.LINHA + "=" * 55 + Cor.RESET)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_inicial():
    limpar_terminal()
    linha_horizontal()
    print(Cor.TEXTO + "BEM VINDO AO SISTEMA RESTAURANTE SOLUTIONS™")
    print("""
    1 - MÓDULO MESAS
    2 - MÓDULO PRATOS
    3 - MÓDULO PEDIDOS
    4 - MÓDULO EXEMPLO
    5 - SAIR
    """)

def main():

    while True:
        limpar_terminal()
        menu_inicial()
        linha_horizontal()
        opcao_inicial = int(input(Cor.TEXTO + "INFORME SUA OPÇÃO: " + Cor.RESET))
        limpar_terminal()

        linha_horizontal()

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
                    limpar_terminal()
                    linha_horizontal()
                    exemplo.menu()
                    linha_horizontal()
                    opcao = input(Cor.TEXTO + "INFORME SUA OPÇÃO: " + Cor.RESET)

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
