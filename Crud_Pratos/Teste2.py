import json
import os

ARQUIVO = 'pratos.json'

def carregar_pratos():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w') as f:
            json.dump([], f)
    with open(ARQUIVO, 'r') as f:
        return json.load(f)

def salvar_pratos(pratos):
    with open(ARQUIVO,"w") as f:
        json.dump(pratos, f, indent=4, ensure_ascii=False)

def cria_novo_prato():
    nome=input("Qual é o nome do prato: ")
    try:
        preco=float(input("Qual é o preço do novo prato: "))
    except ValueError:
        print("Preço invalido")
        return
    categoria=input("Qual é a categoria do prato? Exemplos: principal,bebida,bebida alcoólica,entrada e sobremesa.")

    pratos=carregar_pratos()
    pratos.append({"nome":nome,"preco":preco,"categoria":categoria})
    salvar_pratos(pratos)
    print("Prato salvo com sucesso.")

def lista_pratos():
    pratos=carregar_pratos()
    if not pratos:
        print("Sem pratos salvo no sistema")
        return
    print("Pratos listados:")
    for i,prato in enumerate(pratos,start=1):
        print(f"{i}- {prato['nome']} | R${prato['preco']:.2f} | Categoria: {prato['categoria']}")

def atualizar_prato():
    pratos = carregar_pratos()
    lista_pratos()
    try:
        numero=int(input("Digite o número do prato que deseja atualizar: "))-1
        if 0<=numero<len(pratos):
            nome=input("Digite o novo nome: ")
            preco=float(input("Digite o novo preço: "))
            categoria=input("Degite a nova categoria: ")
            pratos[numero]={"nome":nome,"preco":preco,"categoria":categoria}
            salvar_pratos()
            print("Mudança deita com sucesso")
        else:
            print("Numero invalido.")
    except(ValueError,IndexError):
        print("Entrada invalida.")

def deletar_prato():
    pratos = carregar_pratos()
    lista_pratos()
    try:
        indice = int(input("Digite o número do prato que deseja deletar: ")) - 1
        if 0 <= indice < len(pratos):
            confirm = input(f"Tem certeza que deseja deletar '{pratos[indice]['nome']}'? (s/n): ").lower()
            if confirm == 's':
                pratos.pop(indice)
                salvar_pratos(pratos)
                print("Prato deletado.")
        else:
            print("Número inválido.")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def fazer_pedido():
    pratos = carregar_pratos()
    if not pratos:
        print("Cardápio vazio. Adicione pratos antes de pedir.")
        return

    valortotal = 0.0
    while True:
        print("\nCardápio:")
        for i, prato in enumerate(pratos, start=1):
            print(f"{i}. {prato['nome']} | R${prato['preco']:.2f} | Categoria: {prato['categoria']}")
        print("0. Finalizar Pedido")

        try:
            escolha = int(input("Escolha o número do prato: "))
        except ValueError:
            print("Entrada inválida.")
            continue

        if escolha == 0:
            break

        if 1 <= escolha <= len(pratos):
            try:
                quant = int(input("Quantidade: "))
                preco = pratos[escolha - 1]['preco']
                valor = preco * quant 
                valortotal += valor
                print(f" {quant}x {pratos[escolha - 1]['nome']} adicionados! Subtotal: R${valor:.2f}")
            except ValueError:
                print("Quantidade inválida.")
        else:
            print("Opção inválida.")

    print(f"\nValor total do pedido: R${valortotal:.2f}")

def menu():
    while True:
        print("\nMENU DO SISTEMA")
        print("1. Criar prato")
        print("2. Listar pratos")
        print("3. Atualizar prato")
        print("4. Deletar prato")
        print("5. Fazer pedido")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cria_novo_prato()
        elif opcao == '2':
            lista_pratos()
        elif opcao == '3':
            atualizar_prato()
        elif opcao == '4':
            deletar_prato()
        elif opcao == '5':
            fazer_pedido()
        elif opcao == '6':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
