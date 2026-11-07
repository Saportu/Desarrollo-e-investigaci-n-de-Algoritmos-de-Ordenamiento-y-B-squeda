from radix_sort import radix_sort
from busqueda_binaria import busqueda_binaria
from busqueda_hash import TablaHash

# Radix
assert radix_sort([]) == []
assert radix_sort([5]) == [5]
assert radix_sort([0, 0]) == [0, 0]
assert radix_sort([3, 1, 3, 2]) == [1, 2, 3, 3]
datos = [170, 45, 75, 90, 802, 24, 2, 66]
assert radix_sort(datos) == sorted(datos)
assert datos == [170, 45, 75, 90, 802, 24, 2, 66]   # no modifica la entrada

# Binaria
orden = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
assert busqueda_binaria([], 1) == -1
assert busqueda_binaria(orden, 23) == 5
assert busqueda_binaria(orden, 2) == 0 and busqueda_binaria(orden, 91) == 9
assert busqueda_binaria(orden, 40) == -1

# Hash: con m=7, 15, 22 y 36 caen en la casilla 1 (colisión)
t = TablaHash(7)
for k in [15, 22, 9, 31, 36]:
    t.insertar(k)
assert t.casillas[1] == [15, 22, 36] and t.casillas[2] == [9] and t.casillas[3] == [31]
assert t.buscar(36) and t.buscar(9) and not t.buscar(99)
assert not TablaHash().buscar(1)
peor = TablaHash(7)                           # peor caso: todo en una casilla
for k in [15, 22, 8, 29, 36]:
    peor.insertar(k)
assert peor.casillas[1] == [15, 22, 8, 29, 36]

if __name__ == "__main__":
    print("Radix:", radix_sort(datos))
    print("Binaria 23 ->", busqueda_binaria(orden, 23))
    print("Hash casillas:", t.casillas)
    print("OK")
