from conta import ContaBancaria
c1 = ContaBancaria('Gabriel', 30000)
c2 = ContaBancaria('Alcides', 100)

c1.depositar(30000)
c1.exibir()
c2.depositar(c1.sacar(10000))
c2.exibir()