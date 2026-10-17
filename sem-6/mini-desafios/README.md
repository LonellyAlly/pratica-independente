# Sistema Bancário - POO em Python

Este projeto modela um sistema bancário simples utilizando os principais pilares da Programação Orientada a Objetos em Python.

## Funcionalidades e Conceitos Aplicados
- **Classes e Objetos**: `Conta`, `ContaCorrente`, `ContaPoupanca`.
- **Encapsulamento**: Uso de `@property` para proteger o saldo (`_saldo`).
- **Herança**: Contas específicas herdando da conta genérica.
- **Polimorfismo**: O método de saque possui regras de negócio diferentes dependendo do tipo da conta.
- **Métodos Mágicos**: Implementação de `__init__` e `__str__`.
