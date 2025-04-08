# 💳 Sistema de Conta Bancária em Python

Este projeto simula uma **conta bancária** com funcionalidades básicas como saque, depósito, transferência, extrato, e controle de limite. Ele foi desenvolvido com foco em conceitos de **POO (Programação Orientada a Objetos)** em Python.

## 📌 Funcionalidades

- Criar contas bancárias com número, titular, saldo e limite.
- Visualizar extrato da conta.
- Realizar depósitos e saques.
- Verificar limite disponível para saque.
- Transferir valores entre contas.
- Métodos estáticos para obter códigos bancários.

## 🧱 Estrutura da Classe `Conta`

- Atributos privados:
  - `__numero`
  - `__titular`
  - `__saldo`
  - `__limite`
- Métodos principais:
  - `extrato()`
  - `depositar(valor)`
  - `sacar(valor)`
  - `transferir(valor, destino)`
- Propriedades (`@property`) para acesso seguro aos atributos.
- Métodos estáticos: `codigo_banco()` e `codigos_bancos()`

## 💻 Exemplo de uso

```python
conta1 = Conta(123, "João", 1000, 500)
conta2 = Conta(456, "Maria", 1500, 300)

conta1.depositar(200)
conta1.sacar(500)
conta1.transferir(300, conta2)

print(conta1.saldo)
print(conta2.saldo)
```

## 📎 Requisitos
Python 3.6 ou superior

## 📁 Como usar
Clone este repositório:

```
git clone https://github.com/devcesar7/banco.git
```
Entre no diretório:

```
cd banco
```
Rode o script:

```
python main.py
```

## 📚 Conceitos aplicados
Encapsulamento

Métodos privados e públicos

Propriedades com @property

Métodos estáticos

Simulação de operações bancárias

##🧑‍💻 Autor
Desenvolvido por Cesar Augusto
