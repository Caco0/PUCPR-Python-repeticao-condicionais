# while True:
#     numero = int(input("Informe um numero: "))
#     if numero == 10:
#         break
#     print(numero)


for numero in range(50):
    if numero == 10:
        break  # se trocar break por 'continue' o laço pula
        # o valor listado na comparação do if
    if numero % 2 == 0:
        continue
    print(numero, end=" ")

# # exemplificando o 'continue' para imprimir números impares
# for numero in range(50):
#     if numero % 2 == 0:
#         continue
#     print(numero, end=" ")
