
import logging
from LibrosDB import LibrosDB

if __name__ == "__main__":

    # Configuración básica de logging (puede personalizar el formato y nivel)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)-8s] [%(name)s] %(message)s',
        filename='errores.log',  # si quieres guardar en archivo
        filemode='a',  # append al archivo
        encoding = 'utf-8'
    )

    logger = logging.getLogger("APP")
    logger.debug("Aplicación iniciada")

    db = LibrosDB()

    print(db.get_all_libros())


    id = db.add_libro(
        {"isbn": "978-00-00-000001",
         "titulo":"El Quijote",
         "autor":"Cervantes",
         "editorial":"Desconocida",
         "fecha_publicacion":1600}
    )
    if id > 0:
        print("El id es: ", id)
        libro = db.get_libro(id)
        print(libro)
    else:
        print("No se pudo añadir el libro")


    libro = db.get_libro(100)
    print(libro)

    print(db.get_all_libros())

    db.delete_libro(100)

