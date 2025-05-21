# -criar novo prato não deveria aceita preço negativo
# o CRUD de pedidos
# -pratos devem ter descrição e dizer quais ingredientes tem
# -na função cria_novo_prato(), ínves de aceitar salvar qualquer string em "categoria", fazer uma lista com as possiveis
# categorias que podem ser aceitas:
#
# ´´´
# POSSIVEIS_CATEGORIAS = ["Aperitivos", "Prato Principal", "Sobremesa", "Bebidas", "Bebida alcoólica"]
#     categoria=terminal_bonito.input_bonito("Qual é a categoria do prato? (Aperitivos|Prato Principal|Sobremesa|Bebidas|Bebidas Alcoólica|): ")
#     # muda a primeira letra pra ser maiscúla e o resto minúscula
#     categoria = categoria.capitalize()
#     if categoria not in POSSIVEIS_CATEGORIAS:
#         terminal_bonito.print_bonito("Categoria inválida")
#         return
# ´´´


import json
import os
import terminal_bonito

arquivo = os.path.join(os.path.dirname(__file__), 'dados/cardapio.json')

def carregar_cardapio():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({}, f)
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_cardapio(cardapio):
    with open(arquivo,"w") as f:
        json.dump(cardapio, f, indent=4, ensure_ascii=False)

def criar_novo_item():
    nome=terminal_bonito.input_bonito("Insira aqui o nome do novo prato a ser adicionado ao cardápio: ")
    try:
        preco=float(terminal_bonito.input_bonito("Insira aqui o valor do prato: "))
    except ValueError:
        terminal_bonito.print_bonito("Preço inválido")
        return
    categoria=terminal_bonito.input_bonito("Qual a categoria do prato? (Aperitivos|Prato Principal|Sobremesa|Bebidas|Bebidas Alcoólica|): ")
    cardapio=carregar_cardapio()

    try:
        proximo_id = max( [int(x) for x in cardapio.keys()] ) + 1
    except ValueError:
        proximo_id = 1

    cardapio[proximo_id]={"nome":nome,"preco":preco,"categoria":categoria}
    salvar_cardapio(cardapio)
    terminal_bonito.print_bonito("Prato salvo com sucesso.")

def listar_pratos():
    cardapio=carregar_cardapio()
    if not cardapio:
        terminal_bonito.print_bonito("Sem items salvo no sistema")
        return
    terminal_bonito.print_bonito("Items listados:")
    for i,prato in cardapio.items():
        terminal_bonito.print_bonito(f"{i}- {prato['nome']} | R${prato['preco']:.2f} | Categoria: {prato['categoria']}")

def atualizar_item():
    cardapio = carregar_cardapio()
    listar_pratos()
    try:
        numero=int(terminal_bonito.input_bonito("Digite o número do prato que deseja atualizar: "))
        if 0<=numero<len(cardapio):
            nome=terminal_bonito.input_bonito("Digite o novo nome: ")
            preco=float(terminal_bonito.input_bonito("Digite o novo preço: "))
            categoria=terminal_bonito.input_bonito("Digite a nova categoria: ")
            cardapio[numero]={"nome":nome,"preco":preco,"categoria":categoria}
            salvar_cardapio(cardapio)
            terminal_bonito.print_bonito("Mudança feita com sucesso")
        else:
            terminal_bonito.print_bonito("Numero inválido.")
    except(ValueError,IndexError):
        terminal_bonito.print_bonito("Entrada inválida.")

def deletar_item():
    cardapio = carregar_cardapio()
    listar_pratos()
    try:
        indice = terminal_bonito.input_bonito("Digite o número do prato que deseja deletar: ")
        if indice in cardapio:
            confirm = terminal_bonito.input_bonito(f"Tem certeza que deseja excluir este prato? '{cardapio[indice]['nome']}'? (s/n): ").lower()
            if confirm == 's':
                del cardapio[indice]
                salvar_cardapio(cardapio)
                terminal_bonito.print_bonito("Prato excluido com sucesso.")
        else:
            terminal_bonito.print_bonito("Número inválido.")
    except (ValueError, IndexError):
        terminal_bonito.print_bonito("Entrada inválida.")

def menu():
    while True:
        terminal_bonito.print_bonito("\nMENU DO SISTEMA")
        terminal_bonito.print_bonito("1. Criar prato")
        terminal_bonito.print_bonito("2. Listar pratos")
        terminal_bonito.print_bonito("3. Atualizar prato")
        terminal_bonito.print_bonito("4. Deletar prato")
        terminal_bonito.print_bonito("5. Sair")
        opcao = terminal_bonito.input_bonito("Escolha uma opção: ")

        if opcao == '1':
            criar_novo_item()
        elif opcao == '2':
            listar_pratos()
        elif opcao == '3':
            atualizar_item()
        elif opcao == '4':
            deletar_item()
        elif opcao == '5':
            terminal_bonito.print_bonito("Encerrando o sistema. Até logo!")
            break
        else:
            terminal_bonito.print_bonito("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
