import CRUD_Exemplo as exemplo
import cor
import os

def linha_horizontal(cor_linha):
    print(cor_linha + "=" * 55 + cor.RESET)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_inicial():
    limpar_terminal()
    linha_horizontal(cor.CIANO)
    print(cor.AZUL + "BEM VINDO AO SISTEMA RESTAURANTE SOLUTIONS™")
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
        linha_horizontal(cor.CIANO)
        opcao_inicial = int(input("INFORME SUA OPÇÃO: "))
        limpar_terminal()
        linha_horizontal(cor.CIANO)

        match (opcao_inicial):
            case 1:
                print("em desenvolvimento c:")
            case 4:
                while True:
                    exemplo.exibir_menu()
                    linha_horizontal(cor.CIANO)
                    opcao = input("INFORME SUA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME:\n>>>")
                        idade = input(" DIGITE A IDADE:\n>>>")
                        exemplo.adicionar_usuario(nome, idade)
                    elif opcao == "2":
                        exemplo.listar_usuarios()
                    elif opcao == "3":
                        nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                        nova_idade = input("DIGITE A NOVA IDADE:\n>>>")
                        exemplo.atualizar_usuario(nome_antigo, novo_nome, nova_idade)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        exemplo.excluir_usuario(nome)
                    elif opcao == "5":
                        nome = input("DIGITE O NOME DO USUÁRIO:\n>>>")
                        exemplo.buscar_usuario(nome)
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 5:
                print("🚀 SAINDO...")
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    main()
