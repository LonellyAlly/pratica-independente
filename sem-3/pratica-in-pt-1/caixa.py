def processar_caixa(*precos):
    if not precos:
        return 0, 0, 0
    total_compra = sum(precos)
    item_mais_caro = max(precos)
    media_precos = total_compra / len(precos)
    return total_compra, item_mais_caro, media_precos

if __name__ == "__main__":
    total, mais_caro, media = processar_caixa(15.50, 42.00, 8.90, 100.00)
    print(f"Total: R${total:.2f} | Item mais caro: R${mais_caro:.2f} | Média de preço: R${media:.2f}")
