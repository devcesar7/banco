class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando sua conta...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print("Conta criada com sucesso!!!")

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Deposito de {valor} na conta de {self.__titular}")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f"Saque de {valor} da conta de {self.__titular}")
        else:
            print("ERRO!!!")
            print(f"O valor {valor}, ultrapassou o limite de {self.__limite}")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}