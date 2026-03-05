class Articulo():
    def __init__(self, referencia = "", descripcion = "", precio = 0, stock=0):
        self._referencia = referencia
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock

        @property
        def referencia(self):
            return self._referencia

        @property
        def descripcion(self):
            return self._descripcion

        @property
        def precio(self):
            return self._precio

        @property
        def stock(self):
            return self._stock

        @referencia.setter
        def referencia(self, valor):
            self._referencia = valor

        @descripcion.setter
        def descripcion(self, valor):
            self._descripcion = valor

        @precio.setter
        def precio(self, valor):
            if valor < 0:
                raise ValueError("El precio no puede ser negativo")
            self._precio = valor

        @stock.setter
        def stock(self, valor):
            if valor < 0:
                raise ValueError("El stock no puede ser negativo")
            self._stock = valor


        def to_file(self):
            return f"{self._referencia}|{self._descripcion}|{self._precio}|{self.stock}\n"

        def from_file(self, linea):
            resultado = "|".join(linea)
            self._referencia = resultado[0]
            self._descripcion = resultado[1]
            self._precio = resultado[2]
            self.stock = resultado[3]
