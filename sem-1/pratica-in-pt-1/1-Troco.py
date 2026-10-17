vc = float(input("Insira o valor da compra:"))
vp = float(input("insira o valor pago:"))

while vp < vc:
    faltante = vc - vp
    print(f"O valor pago não foi suficiente. Faltam R${faltante:.2f}")
    
    novo_valor = float(input("Insira o valor restante:"))
    vp += novo_valor
tc = vp - vc
print(f"Pagamento aprovado! O troco é de R${tc:.2f}")
