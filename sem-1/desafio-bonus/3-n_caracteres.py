frase = input("Insira uma frase: ")

num_caracteres = len(frase)
num_palavras = len(frase.split())
frase_maiusculas = frase.upper()

print(f"Nº de caracteres: {num_caracteres}")
print(f"Nº de palavras: {num_palavras}")
print(f"Frase em maiúsculas: {frase_maiusculas}")
