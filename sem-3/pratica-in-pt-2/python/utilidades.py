def dobrar(valor):
    return valor * 2

def eh_par(numero):
    return numero % 2 == 0

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a)."

if __name__ == "__main__":
    print(saudacao("Carlos"))
    print(f"O dobro de 15 é: {dobrar(15)}")
    print(f"O número 10 é par? {eh_par(10)}")
