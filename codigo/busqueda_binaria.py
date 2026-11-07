# sin optimizar: versión iterativa simple, solo sobre lista ya ordenada
def busqueda_binaria(ordenada, objetivo):
    bajo, alto = 0, len(ordenada) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if ordenada[medio] == objetivo:
            return medio                      # encontrado: devuelve el índice
        if ordenada[medio] < objetivo:
            bajo = medio + 1                  # descarta la mitad izquierda
        else:
            alto = medio - 1                  # descarta la mitad derecha
    return -1                                 # no está
