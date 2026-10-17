"""
Sistema Orientado a Objetos - E-commerce (Sprint 6)
Demonstração de POO com Classes Abstratas, Herança, Polimorfismo e Encapsulamento.
"""

from abc import ABC, abstractmethod
import re

class Produto(ABC):
    """Classe abstrata base para todos os produtos."""
    def __init__(self, codigo: int, nome: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, valor: float):
        if valor <= 0:
            raise ValueError(f"O preço do produto '{self.nome}' deve ser maior que zero. (Valor recebido: {valor})")
        self._preco = valor

    @abstractmethod
    def processar_entrega(self) -> str:
        """Método abstrato que deve ser implementado pelas subclasses."""
        pass

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nome} - R${self.preco:.2f}"


class ProdutoFisico(Produto):
    """Produto que necessita de envio físico (frete)."""
    def __init__(self, codigo: int, nome: str, preco: float, peso_kg: float):
        super().__init__(codigo, nome, preco)
        self.peso_kg = peso_kg

    def processar_entrega(self) -> str:
        """Implementação do polimorfismo para produtos físicos."""
        custo_frete = self.peso_kg * 15.0
        return f"Enviando '{self.nome}' via transportadora. Peso: {self.peso_kg}kg | Frete estimado: R${custo_frete:.2f}."

    def __str__(self) -> str:
        return f"{super().__str__()} (Físico - {self.peso_kg}kg)"


class ProdutoDigital(Produto):
    """Produto digital que é entregue via link de download."""
    def __init__(self, codigo: int, nome: str, preco: float, tamanho_mb: float):
        super().__init__(codigo, nome, preco)
        self.tamanho_mb = tamanho_mb

    def processar_entrega(self) -> str:
        """Implementação do polimorfismo para produtos digitais."""
        return f"Gerando link de download seguro para '{self.nome}' ({self.tamanho_mb}MB). Enviando por e-mail."

    def __str__(self) -> str:
        return f"{super().__str__()} (Digital - {self.tamanho_mb}MB)"


class Cliente:
    """Classe representando um cliente do e-commerce."""
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(padrao, valor):
            raise ValueError(f"E-mail inválido para o cliente '{self.nome}': {valor}")
        self._email = valor

    def __str__(self) -> str:
        return f"Cliente: {self.nome} ({self.email})"


class Pedido:
    """Classe que agrega produtos e um cliente para finalizar uma compra."""
    def __init__(self, numero_pedido: int, cliente: Cliente):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        """Adiciona um produto à lista do pedido."""
        self.produtos.append(produto)

    @property
    def total(self) -> float:
        """Calcula dinamicamente o total do pedido."""
        return sum(p.preco for p in self.produtos)

    def finalizar_pedido(self):
        """Finaliza o pedido, demonstrando o polimorfismo na entrega."""
        if not self.produtos:
            print(f"Pedido #{self.numero_pedido} está vazio e não pode ser finalizado.")
            return

        print(f"\n{'='*40}")
        print(f"PROCESSANDO PEDIDO #{self.numero_pedido} - {self.cliente.nome}")
        print(f"{'='*40}")
        for p in self.produtos:
            print(f" - {p.processar_entrega()}")
        print("-" * 40)
        print(f"Total pago: R${self.total:.2f}")
        print("=" * 40)

    def __str__(self) -> str:
        return f"Pedido #{self.numero_pedido} | Cliente: {self.cliente.nome} | Itens: {len(self.produtos)} | Total: R${self.total:.2f}"


def main():
    print("--- INICIANDO SISTEMA DE E-COMMERCE ---\n")

    try:
        produto_invalido = ProdutoFisico(999, "Monitor Quebrado", -50.0, 2.0)
    except ValueError as e:
        print(f"[ERRO CAPTURADO] Falha ao criar produto: {e}")

    try:
        cliente_invalido = Cliente("Usuario Fake", "email_sem_arroba.com")
    except ValueError as e:
        print(f"[ERRO CAPTURADO] Falha ao criar cliente: {e}\n")

    cliente1 = Cliente("Guilherme", "guilherme@email.com")
    cliente2 = Cliente("Ana Laura", "ana.laura@email.com")
    cliente3 = Cliente("Carlos", "carlos.dev@techx.com")

    prod1 = ProdutoFisico(101, "Xiaomi Poco X7 5G", 2100.00, 0.4)
    prod2 = ProdutoFisico(102, "Teclado Mecânico MageGee 60%", 189.90, 0.6)
    prod3 = ProdutoDigital(201, "Curso: AI Agent Fundamentals", 250.00, 1500.0)
    prod4 = ProdutoDigital(202, "E-book: Engenharia de Software", 45.00, 12.5)
    prod5 = ProdutoFisico(103, "Cabo de Áudio Hi-Fi Prata", 85.00, 0.1)

    pedido1 = Pedido(1001, cliente1)
    pedido1.adicionar_produto(prod1)
    pedido1.adicionar_produto(prod2)
    pedido1.adicionar_produto(prod3)

    pedido2 = Pedido(1002, cliente3)
    pedido2.adicionar_produto(prod4)
    pedido2.adicionar_produto(prod5)

    print("--- CATÁLOGO DE PRODUTOS ---")
    for produto in [prod1, prod2, prod3, prod4, prod5]:
        print(produto)

    print("\n--- RESUMO DOS PEDIDOS ---")
    print(pedido1)
    print(pedido2)

    pedido1.finalizar_pedido()
    pedido2.finalizar_pedido()

if __name__ == "__main__":
    main()
