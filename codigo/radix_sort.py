# sin optimizar: solo enteros >= 0, base 10 fija, copia la lista en cada pasada
def radix_sort(datos):
    datos = list(datos)
    if not datos:
        return datos
    exp = 1                                   # 1 = unidades, 10 = decenas, ...
    while max(datos) // exp > 0:
        datos = _ordenar_por_digito(datos, exp)
        exp *= 10
    return datos


def _ordenar_por_digito(datos, exp):          # counting sort estable
    cuenta = [0] * 10
    for x in datos:
        cuenta[(x // exp) % 10] += 1
    for d in range(1, 10):                    # acumulado = posición final
        cuenta[d] += cuenta[d - 1]
    salida = [0] * len(datos)
    for x in reversed(datos):                 # reversed mantiene la estabilidad
        d = (x // exp) % 10
        cuenta[d] -= 1
        salida[cuenta[d]] = x
    return salida
