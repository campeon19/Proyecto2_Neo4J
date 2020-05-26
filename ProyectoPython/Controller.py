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

_menu_iniciar_instrucciones = """
Acontinuacion se le presentaran varias opciones en parejas, debera elejir la que mas le guste para que asi
podamos calcular opciones de juegos que puedan ser de su agrado

"""

class Controller:

    """Constructor de la clase"""
    def __init__(self):
        self.salida = True
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Proyecto123")
        self.tiempoMin = 0
        self.tiempoMax = 0

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

    def Resultados(self, tags, tMin, tMax):
        resultados = self.conexion.searchGameByTagsAndTime(tags, tMin, tMax)
        for _ in range(50):
            print()
        print("Los resultados recomendados segun las caracteristicas de juego que eligio son:\n\n")
        for res in resultados:
            print("\n"+str(res).capitalize()+":")
            c = 0
            for i in resultados[res]:
                print("- "+ resultados[res][c])
                c = c + 1

        input("\n\nPresione enter para volver al menu principal...")

    """Funcion que organiza y realiza las preguntas al usuario"""
    def preguntas(self):
        caracteristicasElejidas = []
        categorias = self.getCharacteristics()
        if (len(categorias) % 2) > 0:
            c = 0
            pos = 0
            for n in range(int(len(categorias) / 2)):
                for _ in range(50):
                    print()
                if c < (len(categorias) - 3):
                    salida = True
                    while salida:
                        print("Escoge el numero de opcion que te guste mas:")
                        print("1."+categorias[c]+" \n2."+categorias[c + 1]+" \n3.Ninguno")
                        opcion = input("\nOpcion: ")

                        if opcion == "1":
                            if categorias[pos] not in caracteristicasElejidas:
                                caracteristicasElejidas.append(categorias[pos])
                            salida = False
                        elif opcion == "2":
                            if categorias[pos + 1] not in caracteristicasElejidas:
                                caracteristicasElejidas.append(categorias[pos + 1])
                            salida = False
                        elif opcion == "3":
                            salida = False
                else:
                    print("Escoge el numero de opcion que te guste mas:")
                    print("1." + categorias[c] + " \n2." + categorias[c + 1] + " \n3."+categorias[c + 2]+" \n4.Ninguno")
                    opcion = input("\nOpcion: ")

                    if opcion == "1":
                        if categorias[pos] not in caracteristicasElejidas:
                            caracteristicasElejidas.append(categorias[pos])
                        salida = False
                    elif opcion == "2":
                        if categorias[pos + 1] not in caracteristicasElejidas:
                            caracteristicasElejidas.append(categorias[pos + 1])
                        salida = False
                    elif opcion == "3":
                        if categorias[pos + 2] not in caracteristicasElejidas:
                            caracteristicasElejidas.append(categorias[pos + 2])
                        salida = False
                    elif opcion == "4":
                        salida = False
                pos = pos + 1
                c = c + 2
        else:
            c = 0
            pos = 0
            for n in range(int(len(categorias) / 2)):
                for _ in range(50):
                    print()

                salida = True
                while salida:
                    print("Escoge el numero de opcion que te guste mas:")
                    print("1." + categorias[c] + " \n2." + categorias[c + 1] + " \n3.Ninguno")
                    opcion = input("\nOpcion: ")

                    if opcion == "1":
                        if categorias[pos] not in caracteristicasElejidas:
                            caracteristicasElejidas.append(categorias[pos])
                        salida = False
                    elif opcion == "2":
                        if categorias[pos + 1] not in caracteristicasElejidas:
                            caracteristicasElejidas.append(categorias[pos + 1])
                        salida = False
                    elif opcion == "3":
                        salida = False
                pos = pos + 1
                c = c + 2
        salida = True
        while salida:
            try:
                self.tiempoMin = float(input("\n\n\nIngrese una cantidad de horas minimas que desea jugar en la semana = "))
                salida = False
            except:
                input("\n\nHas ingresado una cantidad no valida \n\nPresiona enter para volver a intentar...")

        salida = True
        while salida:
            try:
                self.tiempoMax = float(input("\nIngrese una cantidad de horas maximas que desea jugar en la semana = "))
                salida = False
            except:
                input("\n\nHas ingresado una cantidad no valida \n\nPresiona enter para volver a intentar...")

        self.Resultados(caracteristicasElejidas, self.tiempoMin, self.tiempoMax)



    """Funcion para ejecutar la opcion 1"""
    def Iniciar(self):
        for _ in range(50):
            print()
        print(_menu_iniciar_instrucciones)
        input("Presiones enter para continuar...")
        self.preguntas()


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

