def main():
    nomes = []
    while True:
        nome = input("Digite um nome (ou deixe em branco para sair): ").strip()
        if not nome:
            break
        nomes.append(nome)
    if not nomes:
        print("Nenhum nome foi digitado.")
        return
    nomes_unicos_set = set(nomes)
    nomes_ordenados = sorted(nomes_unicos_set)
    tupla_extremos = (nomes_ordenados[0], nomes_ordenados[-1])
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Total de nomes digitados: {len(nomes)}")
    print(f"Total de nomes únicos: {len(nomes_ordenados)}")
    print(f"Lista de nomes ordenada: {nomes_ordenados}")
    print(f"Tupla (Primeiro e Último): {tupla_extremos}")

if __name__ == "__main__":
    main()
