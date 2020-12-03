def subsetSum(pesos: list, valor: int):
    tabela = [[1] * valor] * (len(pesos))

    for indice in range(1, valor):
        tabela[0][indice] = 0

        for segundoIndice in range(1, len(pesos)):
            auxiliar = tabela[segundoIndice - 1][indice]
            if auxiliar == 0 and pesos[segundoIndice] <= indice:
                auxiliar = tabela[segundoIndice - 1][indice - pesos[segundoIndice]]
            tabela[segundoIndice][indice] = auxiliar

    return tabela[len(pesos) - 1][valor - 1]


p = [30, 40, 10, 15, 10, 60, 54]
c = 55

print(subsetSum(p, c))