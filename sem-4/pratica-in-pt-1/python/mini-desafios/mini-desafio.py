def main():
    produtos = [
        {"nome": "Notebook", "preco": 4500.00, "categoria": "Eletrônicos"},
        {"nome": "Mouse", "preco": 120.00, "categoria": "Eletrônicos"},
        {"nome": "Cadeira", "preco": 850.00, "categoria": "Móveis"},
        {"nome": "Mesa", "preco": 1200.00, "categoria": "Móveis"},
        {"nome": "Caderno", "preco": 35.00, "categoria": "Papelaria"}
    ]
    valor_filtro = 500.00
    produtos_acima_valor = [p for p in produtos if p["preco"] > valor_filtro]
    produtos_crescente = sorted(produtos, key=lambda x: x["preco"])
    produtos_decrescente = sorted(produtos, key=lambda x: x["preco"], reverse=True)
    categorias_unicas = set(p["categoria"] for p in produtos)
    precos = [p["preco"] for p in produtos]
    menor_preco = min(precos)
    maior_preco = max(precos)
    media_precos = sum(precos) / len(precos)
    estatisticas = (menor_preco, maior_preco, media_precos)
    print("--- RELATÓRIO DO SISTEMA DE PRODUTOS ---\n")
    print(f"1. Produtos acima de R$ {valor_filtro:.2f}:")
    for p in produtos_acima_valor:
        print(f"   - {p['nome']} (R$ {p['preco']:.2f})")
    print("\n2. Categorias disponíveis:")
    for cat in categorias_unicas:
        print(f"   - {cat}")

    print("\n3. Produtos ordenados por preço (Crescente):")
    for p in produtos_crescente:
        print(f"   - {p['nome']}: R$ {p['preco']:.2f}")

    print("\n4. Estatísticas Gerais (Tupla):")
    print(f"   - Menor preço: R$ {estatisticas[0]:.2f}")
    print(f"   - Maior preço: R$ {estatisticas[1]:.2f}")
    print(f"   - Preço médio: R$ {estatisticas[2]:.2f}")

if __name__ == "__main__":
    main()
