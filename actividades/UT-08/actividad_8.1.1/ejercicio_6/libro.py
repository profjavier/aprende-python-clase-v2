class Libro:
    isbns = []
    num_libros = 0

    def __init__(self, isbn, titulo, autor=None):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        Libro.num_libros += 1
        Libro.isbns.append(isbn)


    def info(self,):
       return  f'''  LIBRO:
        ISBN: {self.isbn}
        TITULO: {self.titulo}
        AUTOR: {self.autor}'''

    def mostrar_titulo(self):
        print(self.titulo.upper())

if __name__ == "__main__":
    libro = Libro("9788408311614","Vera una historia de Amor", 'Juan del Val')
    print(libro.info())
    libro.mostrar_titulo()

    libros = []
    seguir = "S"
    while seguir == "S":
        isbn = input("ISBN: ")
        titulo = input("Ingresa tu titulo: ")
        autor = input("Ingresa tu autor: ")
        libros.append(Libro(isbn, titulo, autor))
        seguir = input("¿Seguir? (s/n): ").upper()

    print(f'Libros creados: {Libro.num_libros}')
