conta_normal = False
conta_estudante = False
saldo = 2000
saque = 2000
cheque_especial = 1000

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso! Você utilizou o cheque especial.")
    else:
        print("Saldo insuficiente para realizar o saque.")
elif conta_estudante:
    if saldo >= saque:
        print("Saque realizado com sucesso da conta Estudante")
    else:
        print("Você não tem saldo suficiente para realizar o saque.")
else:
    print(
        "Você não tem uma conta válida por favor entre em contato com o gerente do seu banco."
    )
