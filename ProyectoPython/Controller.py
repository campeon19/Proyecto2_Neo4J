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
Acontinuacion se le presentaran varias opciones en parejas, debera elegir la que mas le guste para que asi
podamos calcular opciones de juegos que puedan ser de su agrado

"""

class Controller:

    """Constructor de la clase"""
    def __init__(self):
        self.salida = True
        #self.conexion = Conexion("bolt://localhost:11003", "neo4j", "Proyecto123")
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Bruhxd")
        self.tiempoMin = 0
        self.tiempoMax = 0
        self.plataformasElegida = ""

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


    def recomendacionNombre(self, resultados):
        opciones = []
        salida = True
        while salida:
            for n in range(50):
                print()
            print("Elija el numero de juego que desea:\n\n")
            for res in resultados:
                for v in resultados[res]:
                    if v not in opciones:
                        opciones.append(v)
            opciones = sorted(opciones)
            c = 1
            for op in opciones:
                print(str(c)+". "+op)
                c = c + 1
            try:
                opcion = int(input("\nOpcion = "))
                if 0 < opcion <= len(opciones):
                    recomendaciones = self.conexion.recomendaciones_juego(opciones[opcion - 1], self.tiempoMin,
                                                                          self.tiempoMax, self.plataformasElegida)
                    for n in range(50):
                        print()

                    print("Recomendaciones en base a juego elegido '"+str(opciones[opcion - 1])+"':\n\n")
                    if len(recomendaciones) == 0:
                        print("No se encontraron resultados")
                    else:
                        for n in sorted(recomendaciones):
                            print("- "+str(n))

                    input("\n\nPresiona enter para volver al menu principal...")
                    salida = False

            except:
                input("\n\nHas ingresado una opcion no valida \n\nPresiona enter para volver a intentar...")




    def Resultados(self, tags, tMin, tMax, plataforma):
        resultados = self.conexion.searchGameTagsPlatforms(tags, tMin, tMax, plataforma)

        salida = True
        while salida:
            for _ in range(50):
                print()
            print("Los resultados recomendados segun las caracteristicas de juego que eligio son:\n\n")
            if len(resultados) == 0:
                print("No se han encontrado resultados... Vuelva a intentar")
            else:
                print("Plataforma: " + plataforma + "\n")
                for res in resultados:
                    print("\n"+str(res).capitalize()+":")
                    c = 0
                    for i in resultados[res]:
                        print("- " + resultados[res][c])
                        c = c + 1
            try:
                opcion = int(input("\n\n--------------------------------------------"
                                   "\n\nElija el numero de la opcion que desea: \n1.Recomendacion en base a juego "
                                   "\n2.Salir \n\nOpcion = "))

                if opcion == 1:
                    salida = False
                    self.recomendacionNombre(resultados)
                elif opcion == 2:
                    salida = False

            except:
                input("\n\nHas ingresado una opcion no valida \n\nPresiona enter para volver a intentar...")

    """Funcion que organiza y realiza las preguntas al usuario"""
    def preguntas(self):
        caracteristicasElejidas = []
        plataformas = self.conexion.getPlataforms()
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
                        print("Escoge el numero de opcion que te guste mas:\n")
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
                    print("Escoge el numero de opcion que te guste mas:\n")
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
                    print("Escoge el numero de opcion que te guste mas:\n")
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
            print("\n\n\nCuantas horas tiene usted disponible para jugar a la semana? Escoja una opcion:")
            print("1. 1-3 horas\n2. 3-5 horas\n3. 5-7 horas\n4. 7 horas en adelante")
            rangoHoras = input("\nOpcion:")

            if rangoHoras == "1":
                self.tiempoMin = 1
                self.tiempoMax = 3
                salida = False
            elif rangoHoras == "2":
                self.tiempoMin = 3
                self.tiempoMax = 5
                salida = False
            elif rangoHoras == "3":
                self.tiempoMin = 5
                self.tiempoMax = 7
                salida = False
            elif rangoHoras == "4":
                self.tiempoMin = 7
                self.tiempoMax = 20
                salida = False
            else:
                print("Has ingresado una opcion no valida")
        salida = True

        while salida:
            try:
                print("\n\nElije el numero de la plataforma que prefieras:\n")
                c = 1
                for n in plataformas:
                    print(str(c) + ". "+n)
                    c = c + 1
                opcion = int(input("\nOpcion = "))
                if (opcion > 0) and (opcion <= len(plataformas)):
                    self.plataformasElegida = plataformas[opcion - 1]
                    salida = False
                else:
                    input("\n\nHas ingresado una opcion no valida \n\nPresiona enter para volver a intentar...")
            except:
                input("\n\nHas ingresado una cantidad no valida \n\nPresiona enter para volver a intentar...")

        self.Resultados(caracteristicasElejidas, self.tiempoMin, self.tiempoMax, self.plataformasElegida)



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
        input("\nPresiona enter para continuar...")

        while self.salida:
            for _ in range(50):
                print()
            print(_opciones_menu)
            opcion = input("\nOpcion = ")

            if opcion == "1":
                self.Iniciar()
            elif opcion == "2":
                self.close()

