def ficha_do_aluno(**dados):
    print("--- Ficha do Aluno ---")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

if __name__ == "__main__":
    ficha_do_aluno(nome="Ana Silva", idade=22, curso="Ciência da Computação")
