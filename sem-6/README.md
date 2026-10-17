# Sistema de E-commerce - POO (Sprint 6)

Este projeto implementa um sistema de E-commerce robusto para consolidar os pilares da Programação Orientada a Objetos em Python: Herança, Polimorfismo, Encapsulamento e Abstração.

## 🏗️ Diagrama de Classes (Mermaid)

```mermaid
classDiagram
    class Produto {
        <<abstract>>
        +int codigo
        +str nome
        -float _preco
        +processar_entrega()* str
    }
    class ProdutoFisico {
        +float peso_kg
        +processar_entrega() str
    }
    class ProdutoDigital {
        +float tamanho_mb
        +processar_entrega() str
    }

    class Cliente {
        +str nome
        -str _email
    }

    class Pedido {
        +int numero_pedido
        +Cliente cliente
        +list produtos
        +float total
        +adicionar_produto(Produto)
        +finalizar_pedido()
    }

    Produto <|-- ProdutoFisico : Herança
    Produto <|-- ProdutoDigital : Herança
    Pedido o-- Produto : Agregação
    Pedido o-- Cliente : Agregação
