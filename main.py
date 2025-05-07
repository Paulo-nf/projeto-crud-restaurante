# crud pra pratos


# crud pra mesas


# crud pra pedidos



def main():
    while True:
        operacao = int(input(
            """Escolha operação:
            1 - Adicionar Prato
            2 - Remover Prato
            3 - Mudar numero de mesas (mostra numero de mesas atual)
            4 - Alter status de mesa
            4.1 - Para Disponivel
            4.2 - Para Ocupada
            4.3 - Para Reservada
            5 - Cadastrar pedido
            6 - Alterar pedido
            7 - Remover pedido
            8 - Checar estados de pedido
            """
            ))

        NUMERO_DE_OPERACOES = 8
        if operacao < 0 or NUMERO_DE_OPERACOES < operacao:
            print("Entrava inválida")
        else:
            # if op == 1:
            #   alguma_coisa()
            # elif op == 2:
            #   outra_coisa()
            # ...
            continue


