import logging

'''
OBSERVACIÓN: SI ALGUN CAMPO TIENE \n no SE GUARDARÁ CORRECTAMENTE
'''

class ArticulosDao:
    """
    Clase para manejar el almacenamiento de artículos en un fichero de texto.

    Esta clase permite guardar artículos representados como diccionarios en un archivo,
    y registra errores en un archivo de log si ocurre algún problema durante la escritura.

    Cada artículo se guarda en una línea del fichero, separando los campos con '|'.
    """

    def __init__(self, filename="articulos.dat"):
        """
        Inicializa el DAO con el nombre del fichero de datos y configura el logger.

        Args:
            filename (str, optional): Nombre del archivo donde se guardarán los artículos.
                                      Por defecto es 'articulos.dat'.
        """
        self.filename = filename
        self.config_log()

    def config_log(self):
        """
        Configura el logger para registrar eventos y errores en un archivo de log.

        El log se guarda en 'articulos.log' con nivel INFO y formato de fecha/hora,
        nivel de log y mensaje.
        """
        log_file = "../articulos.log"
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def save(self, articulo: dict) -> bool:
        """
        Guarda un artículo en el fichero.

        Args:
            articulo (dict): Diccionario con los campos del artículo:
                             'referencia', 'descripcion', 'precio', 'stock', 'observaciones'.

        Returns:
            bool: True si el artículo se guardó correctamente, False si hubo un error.

        Ejemplo:
            dao = ArticulosDao()
            articulo = {
                "referencia": "A001",
                "descripcion": "Lápiz",
                "precio": 0.5,
                "stock": 100,
                "observaciones": "Sin observaciones"
            }
            dao.save(articulo)
        """
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(f"{articulo.get('referencia','')}|"
                        f"{articulo.get('descripcion','')}|"
                        f"{articulo.get('precio','')}|"
                        f"{articulo.get('stock','')}|"
                        f"{articulo.get('observaciones','')}\n")
                return True
        except Exception as e:
            self.logger.error(f"Error al guardar artículo {articulo.get('referencia','')}: {e}")
            return False

    def find(self, referencia_buscada: str) -> bool:
        """
        Consulta un artículo en el fichero segun la referencia.

        Args:
            referencia_buscada (str): Referencia del articulo buscado.

        Returns:
            articulo (dict): - Diccionario con los campos del artículo:
                                'referencia', 'descripcion', 'precio', 'stock', 'observaciones'.
                             - Devuelve None si no existe.

        Ejemplo:
            dao = ArticulosDao()
            articulo = {
                "referencia": "A001",
                "descripcion": "Lápiz",
                "precio": 0.5,
                "stock": 100,
                "observaciones": "Sin observaciones"
            }
            dao.save(articulo)
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                articulo_str = f.readline().strip()
                articulo = self.str_to_dict(articulo_str)
                while articulo and articulo.get("referencia") != referencia_buscada:
                    articulo_str = f.readline().strip()
                    articulo = self.str_to_dict(articulo_str)

                if articulo:
                    return articulo
        except Exception as e:
            self.logger.error(f"Error al buscar artículo {referencia_buscada}: {e}")

        return None

    def find_all(self) -> list:
        """
        """
        try:
            articulos = []
            with open(self.filename, "r", encoding="utf-8") as f:
                for articulo_str in f.readlines():
                    articulos.append(self.str_to_dict(articulo_str.strip()))
        except Exception as e:
            self.logger.error(f"Error al acceder al fichero: {e}")
        return articulos

    def delete(self, referencia) -> bool:
        """
        """
        borrado = False
        try:
            with open(self.filename, "r", encoding="utf-8") as f_original, open(self.filename+"-TMP", "w", encoding="utf-8") as f_temporal:
                # Vuelca el contenido del archivo original (salvo la referencia) en el archivo temporal
                for articulo_str in f_original.readlines():
                    referencia_row = articulo_str.split("|")[0]
                    if referencia_row != referencia:
                        f_temporal.write(articulo_str)

            # Vuelca todo el contenido del archivo temporal en el original
            with open(self.filename, "w", encoding="utf-8") as f_original, open(self.filename + "-TMP", "r", encoding="utf-8") as f_temporal:
                for articulo_str in f_temporal.readlines():
                    referencia_row = articulo_str.split("|")[0]
                    f_original.write(articulo_str)

            f_temporal =  open(self.filename + "-TMP", "w", encoding="utf-8")
            f_temporal.close()

            # También se puede utilizar shutil para realizar operaciones de copia y borrado de ficheros
            borrado = True
        except Exception as e:
            self.logger.error(f"Error al acceder al fichero: {e}")
        return borrado

    def update(self, referencia, articulo) -> bool:
        """
        """
        borrado = False
        try:
            with open(self.filename, "r", encoding="utf-8") as f_original, open(self.filename+"-TMP", "w", encoding="utf-8") as f_temporal:
                # Vuelca el contenido del archivo original (modificando  el articulo referenciado) en el archivo temporal
                for articulo_str in f_original.readlines():
                    referencia_row = articulo_str.split("|")[0]
                    if referencia_row != referencia:
                        f_temporal.write(articulo_str)
                    else:
                        dato = f"{articulo.get('referencia', '')}|{articulo.get('descripcion', '')}|{articulo.get('precio', '')}|{articulo.get('stock', '')}|{articulo.get('observaciones', '')}\n"
                        f_temporal.write(dato)


            # Vuelca todo el contenido del archivo temporal en el original
            with open(self.filename, "w", encoding="utf-8") as f_original, open(self.filename + "-TMP", "r", encoding="utf-8") as f_temporal:
                for articulo_str in f_temporal.readlines():
                    referencia_row = articulo_str.split("|")[0]
                    f_original.write(articulo_str)

            f_temporal =  open(self.filename + "-TMP", "w", encoding="utf-8")
            f_temporal.close()

            # También se puede utilizar shutil para realizar operaciones de copia y borrado de ficheros
            borrado = True
        except Exception as e:
            self.logger.error(f"Error al acceder al fichero: {e}")
        return borrado

    def delete_all(self) -> bool:
        """
        """
        borrado = False
        try:
            f_original =  open(self.filename, "w", encoding="utf-8")
            f_original.close()
            borrado = True
        except Exception as e:
            self.logger.error(f"Error al acceder al fichero: {e}")
        return borrado

    @staticmethod
    def str_to_dict(articulo_str):
        articulo_arr = articulo_str.split("|")
        articulo = {
            "referencia": articulo_arr[0],
            "descripcion": articulo_arr[1],
            "precio": float(articulo_arr[2]),
            "stock": float(articulo_arr[3]),
            "observaciones": articulo_arr[4]
        }
        return articulo
