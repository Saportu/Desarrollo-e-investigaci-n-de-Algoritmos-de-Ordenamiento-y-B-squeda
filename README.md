# Desarrollo e investigación de algoritmos de ordenamiento y búsqueda

Algoritmos y Estructuras de Datos I, Instituto Tecnológico de Costa Rica, II Semestre 2026.

**Integrantes:** Marco Chavarría León, Santiago Portuguez Hernández, Francisco Ramírez Delgado, Jan Carlo Vargas Araya y Carlos Zhou Fernández.

## Contenido

| Archivo | Algoritmo | Tiempo (mejor / promedio / peor) |
|---|---|---|
| `codigo/radix_sort.py` | Radix Sort LSD base 10 con counting sort estable | O(d·(n+b)) en los tres casos |
| `codigo/busqueda_binaria.py` | Búsqueda binaria iterativa | O(1) / O(log n) / O(log n) |
| `codigo/busqueda_hash.py` | Tabla hash con encadenamiento (m = 7) | O(1) / O(1+α) / O(n) |
| `codigo/test_algoritmos.py` | Pruebas de los tres algoritmos | |
| `presentacion/Presentacion.pdf` | Presentación (23 diapositivas) | |

Las versiones son **sin optimizaciones**; la primera línea de cada archivo indica su límite.

## Ejecutar las pruebas

Necesita Python 3, sin librerías adicionales:

```
cd codigo
python3 test_algoritmos.py
```

Debe imprimir `OK`.
