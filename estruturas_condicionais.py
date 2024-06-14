MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade! Pode tirar CNH")
else:
    print("Você é menor de idade! Não pode tirar CNH")
# ------------------------------------------------------

if idade >= MAIOR_IDADE:
    print("Você é maior de idade! Pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Você é menor de idade, mas pode fazer aulas teóricas")
else:
    print("Ainda não pode tirar CNH.")
