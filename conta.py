class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando sua conta...")
        # Atributos privados da conta
        self.__numero = numero        # Número da conta
        self.__titular = titular      # Nome do titular da conta
        self.__saldo = saldo          # Saldo atual da conta
        self.__limite = limite        # Limite extra permitido para saque
        print("Conta criada com sucesso!!!")

    def extrato(self):
        # Exibe o saldo e o nome do titular
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        # Adiciona valor ao saldo
        self.__saldo += valor
        print(f"Deposito de {valor} na conta de {self.__titular}")

    def __pode_sacar(self, valor_a_sacar):
        # Verifica se é possível sacar o valor solicitado
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        # Realiza o saque se houver saldo ou limite suficiente
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f"Saque de {valor} da conta de {self.__titular}")
        else:
            print("ERRO!!!")
            print(f"O valor {valor}, ultrapassou o limite de {self.__limite}")

    def transferir(self, valor, destino):
        # Transfere valor desta conta para outra (destino)
        self.sacar(valor)           # Primeiro saca da conta atual
        destino.depositar(valor)    # Depois deposita na conta de destino

    # GETTER para saldo
    @property
    def saldo(self):
        return self.__saldo

    # GETTER para titular
    @property
    def titular(self):
        return self.__titular

    # GETTER e SETTER para limite
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Método estático: retorna o código do banco padrão
    @staticmethod
    def codigo_banco():
        return "001"

    # Método estático: retorna códigos de vários bancos
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
