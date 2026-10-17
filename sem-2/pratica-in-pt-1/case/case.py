print("Menu de Operações:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao_escolhida = input("Escolha uma operação (1-4): ")

primeiro_numero = float(input("Insira o primeiro número: "))
segundo_numero = float(input("Insira o segundo número: "))

match opcao_escolhida:
    case "1":
        resultado_operacao = primeiro_numero + segundo_numero
        print(f"Resultado da adição: {resultado_operacao}")
    case "2":
        resultado_operacao = primeiro_numero - segundo_numero
        print(f"Resultado da subtração: {resultado_operacao}")
    case "3":
        resultado_operacao = primeiro_numero * segundo_numero
        print(f"Resultado da multiplicação: {resultado_operacao}")
    case "4":
        if segundo_numero == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado_operacao = primeiro_numero / segundo_numero
            print(f"Resultado da divisão: {resultado_operacao}")
    case _:
        print("Opção inválida.")
