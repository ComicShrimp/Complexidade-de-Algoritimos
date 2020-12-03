def intervaloDisjunto(
    inicio: list, fim: list, intervalo_inicio: int, intervalo_fim: int
):
    x = [0]
    k = intervalo_inicio

    for indice in range(1, intervalo_fim):
        if inicio[indice] > fim[k]:
            x.append(indice)
            k = indice
    return x


a = [6, 9, 7, 18, 1, 23, 25, 30]
b = [15, 15, 16, 24, 26, 28, 30, 34]
p = 1
r = 8

print(intervaloDisjunto(a, b, p, r))
