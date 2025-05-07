import json
import os

# Definindo o caminho do arquivo no escopo global
arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.json')


def carregar_usuarios():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

    # Carrega o conteúdo do arquivo
    with open(arquivo, 'r') as f:
        return json.load(f)

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AZUL = '\033[94m'
    RESET = '\033[0m'

def exibir_menu():
    print(cor.AZUL + "MENU:")
    print("""
    1. ADICIONAR USUÁRIO
    2. LISTAR USUÁRIOS
    3. ATUALIZAR USUÁRIO
    4. EXCLUIR USUÁRIO
    5. LISTAR UM USUÁRIO
    6. VOLTAR AO MENU ANTERIOR
""" + cor.RESET)

def adicionar_usuario(nome, idade):
    usuarios = carregar_usuarios()

    usuarios.append({'nome': nome, 'idade': idade})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def listar_usuarios():
    usuarios = carregar_usuarios()

    if usuarios:
        print("=" *50)
        print("LISTA DE USUÁRIOS:")
        print("-" *50)
        for usuario in usuarios:
            print("*" *50)
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def atualizar_usuario(nome_antigo, novo_nome, nova_idade):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['nome'] == nome_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            break

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(nome):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)
    print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_usuario(nome):
    usuarios = carregar_usuarios()

    encontrado = False

    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            encontrado = True
    if not encontrado:
        print("😒 NENHUM USUÁRIO CADASTRADO.")
