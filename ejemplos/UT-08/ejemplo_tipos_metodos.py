
class MiFichero:
    path_name = "./mi_aplicacion/"

    def __init__(self, filename):
        self.filename = filename

    '''
    Métodos CRUD
    '''
    def save(self, linea) -> bool:
        try:
            with open(self.path_name + self.filename, "a") as f:
                f.write(linea)
                return True
        except Exception as e:
            return False

    @classmethod
    def set_path_name(cls, path_name):
        cls.path_name = path_name

if __name__ == '__main__':
    mifi_1 = MiFichero("mi_aplicacion_1.txt")
    mifi_1.save("Nueva linea")
    mifi_2 = MiFichero("mi_aplicacion_2.txt")
    mifi_2.save("Nueva linea")

    MiFichero.set_path_name("./mi_aplicacion2/")
    mifi_1 = MiFichero("mi_aplicacion_1.txt")
    mifi_1.save("Nueva linea2")
    mifi_2 = MiFichero("mi_aplicacion_2.txt")
    mifi_2.save("Nueva linea2")
