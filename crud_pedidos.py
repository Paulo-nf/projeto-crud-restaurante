import json
import os
from datetime import datetime

ARQ_PEDIDOS = 'dados/pedidos.json'
ARQ_CARDAPIO = 'dados/cardapio.json'
ARQ_MESAS = 'dados/mesas.json'

def carregar_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r') as f:
            return json.load(f)
    return {}

def salvar_json(dados, caminho):
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=4)

def verificar_item_cardapio(cardapio, id_item):
    return str(id_item) in cardapio

def mesa_disponivel(mesas, id_mesa):
    return mesas.get(str(id_mesa), {}).get("status") == "livre"

def ocupar_mesa(mesas, id_mesa):
    mesas[str(id_mesa)] = {"status": "ocupada"}
    salvar_json(mesas, ARQ_MESAS)

def criar_pedido():
    pedidos = carregar_json(ARQ_PEDIDOS)
    cardapio = carregar_json(ARQ_CARDAPIO)
    mesas = carregar_json(ARQ_MESAS)

    id_mesa = input("Número da mesa: ")

    if not mesa_disponivel(mesas, id_mesa):
        print("Mesa ocupada ou inexistente.")
        return

    itens = []
    while True:
        id_item = input("ID do item do cardápio (0 para sair): ")
        if id_item == '0':
            break
        if not verificar_item_cardapio(cardapio, id_item):
            print("Item inválido.")
            continue

        quantidade = int(input("Quantidade: "))
        obs = input("Observação (opcional): ")

        itens.append({
            "id_cardapio": int(id_item),
            "quantidade": quantidade,
            "observacao": obs
        })

    if not itens:
        print("Pedido vazio. Cancelado.")
        return

    novo_id = str(max([int(k) for k in pedidos] + [0]) + 1)
    pedidos[novo_id] = {
        "mesa": int(id_mesa),
        "itens": itens,
        "status": "em preparo",
        "horario": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    ocupar_mesa(mesas, id_mesa)
    salvar_json(pedidos, ARQ_PEDIDOS)
    print(f"Pedido {novo_id} criado com sucesso.")

def listar_pedidos():
    pedidos = carregar_json(ARQ_PEDIDOS)
    cardapio = carregar_json(ARQ_CARDAPIO)

    if not pedidos:
        print("Nenhum pedido encontrado.")
        return

    for pid, pedido in pedidos.items():
        print(f"\nPedido ID: {pid}")
        print(f" Mesa: {pedido['mesa']}")
        print(f" Status: {pedido['status']}")
        print(f" Horário: {pedido['horario']}")
        print(" Itens:")
        total = 0
        for item in pedido['itens']:
            id_item = str(item["id_cardapio"])
            nome = cardapio.get(id_item, {}).get("nome", "Desconhecido")
            preco = cardapio.get(id_item, {}).get("preco", 0.0)
            subtotal = preco * item["quantidade"]
            total += subtotal
            print(f"  - {nome} x{item['quantidade']} (R${subtotal:.2f}) - {item['observacao']}")
        print(f" Total: R${total:.2f}")
        print("-" * 40)

def atualizar_status_pedido():
    pedidos = carregar_json(ARQ_PEDIDOS)
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return

    id_pedido = input("ID do pedido a atualizar: ")
    if id_pedido not in pedidos:
        print("Pedido não encontrado.")
        return

    print("Status atual:", pedidos[id_pedido]["status"])
    print("1 - Em preparo")
    print("2 - Pronto")
    print("3 - Entregue")
    opcao = input("Novo status (1-3): ")

    status_map = {"1": "em preparo", "2": "pronto", "3": "entregue"}
    if opcao in status_map:
        pedidos[id_pedido]["status"] = status_map[opcao]
        salvar_json(pedidos, ARQ_PEDIDOS)
        print("Status atualizado.")
    else:
        print("Opção inválida.")

def menu_pedidos():
    while True:
        print("\n=== MENU DE PEDIDOS ===")
        print("1. Criar novo pedido")
        print("2. Listar pedidos")
        print("3. Atualizar status de pedido")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_pedido()
        elif opcao == '2':
            listar_pedidos()
        elif opcao == '3':
            atualizar_status_pedido()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_pedidos()
