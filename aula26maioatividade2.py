#solicite a quantidade de itens que o usuário quer adicionar
quantidade = int(input("Quantos itens deseja adicionar á lista de compras?"))
#Iniciando a lista de compras
lista_compras = []
#Loop para adicionar os itens
for i in range(quantidade):
    item = input(f"Digite o nome do item {i + 1}:")
    lista_compras.append(item)

    #Exibe a lista completa
    print("\nLista completa de itens:")
    for item in lista_compras:
        print(f"-{item}")
        #Exibe a quantidade de itens
        print(f"\nQuantidade de itens na lista: {len(lista_compras)}")
        #Exibe a lista em ordem alfábetica
        lista_ordenada = sorted(lista_compras)
        print("\nLista em ordem alfabética:")
        for item in lista_ordenada:
            print(f"-{item}")
                                                 