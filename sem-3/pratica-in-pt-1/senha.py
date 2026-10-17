def validar_senha(senha):
    return len(senha) >= 8

if __name__ == "__main__":
    senha_ok = validar_senha("python123")
    print(f"A senha tem 8 ou mais caracteres? {senha_ok}")

