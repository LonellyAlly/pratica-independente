import csv
import json
import re

class DadoInvalidoError(Exception):
    """Exceção levantada quando um dado (email ou CPF) não passa na validação."""
    pass

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao, email):
        raise DadoInvalidoError(f"E-mail inválido: {email}")
    return True

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if not re.match(padrao, cpf):
        raise DadoInvalidoError(f"CPF inválido: {cpf}")
    return True

def processar_clientes(arquivo_entrada, arquivo_saida):
    clientes_validos = []
    erros = []
    linhas_processadas = 0

    try:
        with open(arquivo_entrada, mode='r', encoding='utf-8') as file:
            leitor_csv = csv.DictReader(file)
            for linha in leitor_csv:
                linhas_processadas += 1
                nome = linha.get('nome', 'Desconhecido')
                email = linha.get('email', '')
                cpf = linha.get('cpf', '')

                try:
                    validar_email(email)
                    validar_cpf(cpf)
                except DadoInvalidoError as e:
                    erros.append({"nome": nome, "erro": str(e)})
                else:
                    clientes_validos.append({"nome": nome, "email": email, "cpf": cpf})

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo: {e}")
        return
    finally:
        print("Processo de leitura finalizado.\n")

    try:
        with open(arquivo_saida, mode='w', encoding='utf-8') as file:
            json.dump(clientes_validos, file, indent=4, ensure_ascii=False)
    except IOError:
        print(f"Erro ao salvar o arquivo '{arquivo_saida}'.")
    else:
        print("--- RELATÓRIO DE PROCESSAMENTO ---")
        print(f"Total de registros analisados: {linhas_processadas}")
        print(f"Clientes válidos salvos: {len(clientes_validos)}")
        print(f"Registros com erro (ignorados): {len(erros)}")
        if erros:
            print("\nDetalhes dos erros:")
            for erro in erros:
                print(f" - {erro['nome']}: {erro['erro']}")
        print(f"\nDados válidos exportados para: {arquivo_saida}")

if __name__ == "__main__":
    processar_clientes('clientes.csv', 'clientes_validos.json')
