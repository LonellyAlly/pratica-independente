"""
Módulo de Sistema Bancário.
Demonstração de POO com Classes, Encapsulamento, Herança e Polimorfismo.
"""

class Conta:
    """Classe base que representa uma conta bancária genérica."""
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def titular(self) -> str:
        """Retorna o nome do titular da conta."""
        return self._titular

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual da conta (Encapsulamento)."""
        return self._saldo

    def depositar(self, valor: float):
        """Deposita um valor positivo na conta."""
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso na conta de {self.titular}.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor: float) -> bool:
        """
        Saca um valor da conta, se houver saldo suficiente.
        Este método será reescrito nas subclasses (Polimorfismo).
        """
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self._saldo:.2f}")
            return True
        else:
            print(f"Saldo insuficiente para saque de R${valor:.2f}.")
            return False

    def __str__(self) -> str:
        """Representação em string do objeto."""
        return f"Conta de {self.titular} | Saldo: R${self.saldo:.2f}"


class ContaCorrente(Conta):
    """Classe derivada que representa uma Conta Corrente com cheque especial (Herança)."""
    def __init__(self, titular: str, saldo_inicial: float = 0.0, limite_cheque_especial: float = 500.0):
        super().__init__(titular, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor: float) -> bool:
        """Saca um valor, permitindo o uso do cheque especial se necessário."""
        saldo_disponivel = self._saldo + self.limite_cheque_especial
        if valor > 0 and saldo_disponivel >= valor:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} aprovado (Conta Corrente). Novo saldo: R${self._saldo:.2f}")
            return True
        else:
            print(f"Saque de R${valor:.2f} negado. Limite do cheque especial excedido.")
            return False

    def __str__(self) -> str:
        return f"Conta Corrente de {self.titular} | Saldo: R${self.saldo:.2f} | Limite: R${self.limite_cheque_especial:.2f}"


class ContaPoupanca(Conta):
    """Classe derivada que representa uma Conta Poupança com rendimento (Herança)."""
    def __init__(self, titular: str, saldo_inicial: float = 0.0, taxa_rendimento: float = 0.05):
        super().__init__(titular, saldo_inicial)
        self.taxa_rendimento = taxa_rendimento

    def render_juros(self):
        """Aplica a taxa de rendimento ao saldo atual."""
        rendimento = self._saldo * self.taxa_rendimento
        self._saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado. Novo saldo: R${self._saldo:.2f}")


    def __str__(self) -> str:
        return f"Conta Poupança de {self.titular} | Saldo: R${self.saldo:.2f} | Taxa: {self.taxa_rendimento*100}%"


def main():
    print("--- INICIANDO TESTES DO SISTEMA BANCÁRIO ---\n")

    cc = ContaCorrente(titular="Guilherme", saldo_inicial=1000.0, limite_cheque_especial=500.0)
    cp = ContaPoupanca(titular="Ana", saldo_inicial=500.0)

    print("Estado inicial das contas:")
    print(cc)
    print(cp)
    print("-" * 40)

    print(f"Titular acessado via property: {cc.titular}")
    print("\n--- Operações Conta Corrente (Guilherme) ---")
    cc.depositar(200)
    cc.sacar(1500)
    cc.sacar(300)

    print("\n--- Operações Conta Poupança (Ana) ---")
    cp.depositar(100)
    cp.render_juros()
    cp.sacar(700)
    cp.sacar(130)

    print("\n--- Estado final das contas ---")
    print(cc)
    print(cp)

if __name__ == "__main__":
    main()
