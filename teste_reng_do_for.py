start = int(input("Digite o valor do start para o laço 'for': "))
stop = int(input("Digite o valor do stop para o laço 'for': "))
step = int(input("Digite o valor do step para o laço 'for': "))


def laco_for(valor_start: int, valor_stop: int, valor_step: int):
    """_Função que lança o start stop e o step do laço for_

    Args:
        valor_start (_type_): _int_
        valor_stop (_type_): _int_
        valor_step (_type_): _int_
    """
    for i in range(valor_start, valor_stop, valor_step):
        print(i, end=" ")


laco_for(start, stop, step)
