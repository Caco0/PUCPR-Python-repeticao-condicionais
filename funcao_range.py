num = int(input("Digite um numero para calcular a tabuada: "))


def tabuada(valor):
    """_Função que calcula a tabuada com range entre 1 e 11
    com resultado entre 1 e 10_

    Args:
        valor (_type_): _int_
    """
    for i in range(1, 11):
        print(f"{valor} x {i} = {valor * i}")


tabuada(num)
