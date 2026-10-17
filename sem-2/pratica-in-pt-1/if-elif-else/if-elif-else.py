idade_cliente = int(input("Insira a idade do cliente: "))
renda_cliente = float(input("Insira a renda do cliente: "))

if idade_cliente < 18:
    classificacao_cliente = "Bronze"
elif renda_cliente >= 10000:
    classificacao_cliente = "Diamante"
elif renda_cliente >= 5000:
    classificacao_cliente = "Ouro"
elif renda_cliente >= 2000:
    classificacao_cliente = "Prata"
else:
    classificacao_cliente = "Bronze"

print(f"Classificação do cliente: {classificacao_cliente}")
