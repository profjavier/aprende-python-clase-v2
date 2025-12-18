from time import sleep


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.esta_arrancado = False


    def acelerar(self, km_h): # en Km/h
        if self.esta_arrancado:
            self.velocidad += km_h

    def frenar(self, km_h):  # en porcentace sw l velocidad
        if self.esta_arrancado:
            # self.velocidad = self.velocidad * (1 - decremento / 100)
            self.velocidad = max(self.velocidad - km_h, 0)

    def arrancar_motor(self):
        if not self.esta_arrancado:
            self.esta_arrancado = True
        else:
            raise "¡Vas a estropear el motor!"

    def parar_motor(self):
       self.esta_arrancado = False

if __name__ == "__main__":
    # coche = Vehiculo("Toyota", "Yaris")
    # coche.arrancar_motor()
    # # coche.arrancar_motor()
    #
    # print("Velocidad actual: ",coche.velocidad)
    # print("Acelerando")
    # for i in range(5):
    #     coche.acelerar(i)
    #     print("Velocidad actual: ",coche.velocidad)
    #     sleep(1)
    # print("Frenando")
    # for i in range(5):
    #     coche.frenar(i)
    #     print("Velocidad actual: ", coche.velocidad)
    #     sleep(1)
    coche = Vehiculo("Toyota", "Yaris")
    try:
        coche.arrancar_motor()
        coche.arrancar_motor()

        print("Velocidad actual: ",coche.velocidad)
        print("Acelerando")
        for i in range(5):
            coche.acelerar(i)
            print("Velocidad actual: ",coche.velocidad)
            sleep(1)
        print("Frenando")
        for i in range(5):
            coche.frenar(i)
            print("Velocidad actual: ", coche.velocidad)
            sleep(1)
    except Exception as ex:
        print(ex)
