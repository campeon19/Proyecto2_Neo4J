from Conexion import Conexion

bienvenido = """
###################################################################################################
###################################################################################################
###                                                                                             ###
###     @@@@@@@  @@  @@@@@@  @@@@   @@  @@      @@  @@@@@@  @@@@   @@  @@  @@@@@@   @@@@@@@@    ###
###     @@   @@  @@  @@      @@ @@  @@   @@    @@   @@      @@ @@  @@  @@  @@  @@@  @@    @@    ###
###     @@ @@    @@  @@@@@@  @@  @@ @@    @@  @@    @@@@@@  @@  @@ @@  @@  @@   @@  @@    @@    ###
###     @@   @@  @@  @@      @@   @@@@     @@@@     @@      @@   @@@@  @@  @@  @@@  @@    @@    ###
###     @@@@@@@  @@  @@@@@@  @@    @@@      @@      @@@@@@  @@    @@@  @@  @@@@@@   @@@@@@@@    ###
###                                                                                             ###
###################################################################################################
###################################################################################################
"""


_opciones_menu = """
Elige el numero de la opcion que desees:

1. Iniciar
2. Salir
"""

class Controller:

    """Constructor de la clase"""
    def __init__(self):
        self.salida = True
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Proyecto123")

    def searchTimeTags(self, tags, tMin, tMax):
        print(self.conexion.searchGameByTagsAndTime(tags, tMin, tMax))

    def getCharacteristics(self):
        return self.conexion.getCharacteristics()

    """Funcion para obtener todos los nombres de los nodos"""
    def getNombres(self):
        print(self.conexion.getNombres())

    """Funcion para cerrar la conexion"""
    def close(self):
        self.conexion.close()
        self.salida = False
        print("\n------ Fin del programa ------")
        exit(0)

    """Funcion para ejecutar la opcion 1"""
    def Iniciar(self):
        print()

    """Funcion para desplegar el menu y realizar las acciones"""
    def menu(self):
        for _ in range(50):
            print()
        print(bienvenido)
        input("\nPesiona enter para continuar...")

        while self.salida:
            for _ in range(50):
                print()
            print(_opciones_menu)
            opcion = input("\nOpcion = ")

            if opcion == "1":
                self.Iniciar()
            elif opcion == "2":
                self.close()

