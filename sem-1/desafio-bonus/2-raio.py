import math

raio = float(input("Insira o raio do círculo: "))

area = math.pi * (raio ** 2)
circunferencia = 2 * math.pi * raio

print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")
