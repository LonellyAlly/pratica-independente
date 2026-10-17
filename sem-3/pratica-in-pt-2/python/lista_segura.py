def adicionar_item_seguro(lista_original, novo_item):
    lista_copia = lista_original.copy()
    lista_copia.append(novo_item)
    return lista_copia

if __name__ == "__main__":
    lista_base = ["Maçã", "Banana"]
    nova_lista = adicionar_item_seguro(lista_base, "Uva")
    print(f"Lista Original: {lista_base}")
    print(f"Nova Lista: {nova_lista}")
