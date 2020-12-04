# Soma de subconjuntos


def subsetSum(pesos: list, valor: int):
    if valor < 1 or len(pesos) == 0:
        return None

    if pesos[0] == valor:
        return [pesos[0]]

    valores = subsetSum(pesos[1:], (valor - pesos[0]))

    if valores:
        return [pesos[0]] + valores
    else:
        return subsetSum(pesos[1:], valor)


p = [30, 40, 10, 15, 10, 60, 54]
c = 60

print(subsetSum(p, c))