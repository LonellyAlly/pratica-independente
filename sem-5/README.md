# Sistema de Análise de Dados - Cadastro de Clientes (Sprint 5)

## Objetivo
Este projeto lê uma base de clientes em formato CSV, valida as informações de contato e documentação utilizando Expressões Regulares (Regex), trata possíveis exceções e exporta os dados válidos para um arquivo JSON, gerando um relatório no terminal.

## Justificativa das Validações (Regex)
- **E-mail (`r"^[\w\.-]+@[\w\.-]+\.\w+$"`):** Garante que o e-mail possua um formato padrão, contendo texto, um símbolo `@`, um domínio e uma extensão (ex: `.com`).
- **CPF (`r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"`):** Garante que o CPF esteja estritamente no formato brasileiro com pontuação `XXX.XXX.XXX-XX`.

## Explicação das Exceções Tratadas
- `FileNotFoundError`: Captura o erro caso o arquivo `clientes.csv` não exista no diretório.
- `IOError`: Captura falhas no momento de gravar o arquivo de saída `clientes_validos.json`.
- `DadoInvalidoError` (Personalizada): Exceção criada especificamente para sinalizar que o regex identificou um dado fora do padrão de negócio exigido (e-mail ou CPF mal formatado).
- `try/except/else/finally`: O `else` é usado para adicionar o cliente à lista apenas se nenhuma exceção for levantada. O `finally` garante a exibição de uma mensagem indicando o fim da etapa de leitura, independentemente de falhas.

## Exemplos de Entrada e Saída
**Entrada (`clientes.csv`):**
```csv
nome,email,cpf
João Silva,joao@email.com,123.456.789-00
Maria Souza,maria.souza@email,987.654.321-11
