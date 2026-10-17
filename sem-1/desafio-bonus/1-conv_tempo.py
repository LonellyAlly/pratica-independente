while True:
    try:
        total_segundos = int(input("Insira o tempo em segundos: "))
        if total_segundos < 0:
            print("Valor inválido! O tempo não pode ser negativo. Tente novamente.\n")
        else:
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.\n")

dias = total_segundos // 86400
resto_segundos = total_segundos % 86400
horas = resto_segundos // 3600
resto_segundos %= 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60

print(f"\n{total_segundos} segundos equivalem a:")
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
