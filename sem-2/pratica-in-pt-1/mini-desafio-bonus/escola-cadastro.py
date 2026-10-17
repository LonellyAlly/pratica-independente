total_cadastros = 0
qtd_aluno = 0
qtd_professor = 0
qtd_funcionario = 0
nomes_cadastrados = []

while True:
    comando_usuario = input("\nDigite qualquer tecla para iniciar/continuar ou 'sair' para encerrar: ").strip().lower()
    if comando_usuario == "sair":
        break
    quantidade_lote = int(input("Quantos cadastros deseja realizar agora? "))
    for _ in range(quantidade_lote):
        nome_pessoa = input("\nNome: ")
        idade_pessoa = int(input("Idade: "))
        if idade_pessoa < 0:
            print("Erro: Idade inválida.")
        elif idade_pessoa < 18:
            print("Erro: Cadastro negado. A idade mínima é 18 anos.")
        else:
            tipo_cadastro = input("Tipo (1 - Aluno, 2 - Professor, 3 - Funcionário): ")
            match tipo_cadastro:
                case "1":
                    qtd_aluno += 1
                    total_cadastros += 1
                    nomes_cadastrados.append(nome_pessoa)
                    print(f"Aluno(a) {nome_pessoa} cadastrado(a) com sucesso!")
                case "2":
                    qtd_professor += 1
                    total_cadastros += 1
                    nomes_cadastrados.append(nome_pessoa)
                    print(f"Professor(a) {nome_pessoa} cadastrado(a) com sucesso!")
                case "3":
                    qtd_funcionario += 1
                    total_cadastros += 1
                    nomes_cadastrados.append(nome_pessoa)
                    print(f"Funcionário(a) {nome_pessoa} cadastrado(a) com sucesso!")
                case _:
                    print("Erro: Tipo de cadastro inválido.")

print(f"\n--- RESUMO DOS CADASTROS ---")
print(f"Quantidade total de cadastros: {total_cadastros}")
print(f"Alunos: {qtd_aluno}")
print(f"Professores: {qtd_professor}")
print(f"Funcionários: {qtd_funcionario}")

print("\nLista dos nomes cadastrados:")
for nome in nomes_cadastrados:
    print(f"- {nome}")
