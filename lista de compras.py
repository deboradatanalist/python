#lista de compra
lista_compras = []
while True:
    print("\nOpções")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar a lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)
        print("foi adicionado à lista de compras.")

    elif opcao =="2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} foi removido da lista")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("\n Lista de Compras")
        if not lista_compras:
            print("A lista está vazia")
        else:
            for i, item in enumerate(sorted(lista_compras), start=1):
                print(f"{i}. {item}")
    elif opcao == "4":
        print("Saindo do Programa")
        break
    else:
        print("Opção Inválida!, digite uma opção Valida")