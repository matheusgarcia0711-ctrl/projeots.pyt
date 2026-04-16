class ContaBancaria:
    # construtor
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado.")

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")


# exemplo
conta = ContaBancaria("João", 1000)

conta.depositar(200)
conta.sacar(150)
conta.ver_saldo()