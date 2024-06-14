texto = input("Digite um texto: ")

VOGAIS = "AEIOU"


def percorre_palavra(palavra):
    """_função que percorre letras e retorna as vogais_

    Args:
        palavra (_type_): _String_
    """
    for letra in palavra:
        if letra.upper() in VOGAIS:
            print(letra, end="")
    else:
        print()  # adiciona uma quebra de linha
        print("Final do laço")


percorre_palavra(texto)
