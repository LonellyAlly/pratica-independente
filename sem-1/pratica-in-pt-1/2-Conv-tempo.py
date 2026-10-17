while True:
    try:
        total_segundos = int(input("Insira o tempo em segundos: "))
        if total_segundos < 0:
            print("Valor inválido! O tempo não pode ser negativo. Tente novamente:")
        else:
            break
    except ValueError:
        print("Entrada inválida! Por favor digite apenas números inteiros.\n")
horas = total_segundos // 3600
resto_segundos = total_segundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60

print(f"\n{total_segundos} segundos equivalem a:")
print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
