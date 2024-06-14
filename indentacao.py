def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado")
    else:
        print("saldo insuficiente")


def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"deposito realizado com sucesso saldo atua R${saldo},00")


print("Obrigado por ser nosso cliente Bom dia!")
sacar(100)
sacar(600)
sacar(500)
depositar(250)
