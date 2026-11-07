# sin optimizar: m fijo, sin rehashing; colisiones con encadenamiento
class TablaHash:
    def __init__(self, m=7):
        self.m = m
        self.casillas = [[] for _ in range(m)]

    def _h(self, clave):
        return clave % self.m                 # función hash: módulo

    def insertar(self, clave):
        self.casillas[self._h(clave)].append(clave)

    def buscar(self, clave):
        return clave in self.casillas[self._h(clave)]
