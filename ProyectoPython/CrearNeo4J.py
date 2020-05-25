from Conexion import Conexion

class CrearNeo4j:

    def __init__(self):
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Proyecto123")

    def leerTxt(self):
        archivo = open("BasedeDatos.txt", mode="r", encoding="utf-8")
        lineas = []
        for linea in archivo.readlines():
            lineas.append(linea.replace("\n", ""))
        archivo.close()
        return lineas

    def fillBase(self):
        juegos = self.leerTxt()
        for juego in juegos:
            split = juego.split(", ")
            nombre = split.pop(0)
            tags = []
            for n in range(len(split)):
                tags.append(split[n].lower())
            self.conexion.createNode(nombre, tags)



    def close(self):
        self.conexion.close()

    def caracteristicas(self):
        archivo = open("BasedeDatos.txt", mode="r", encoding="utf-8")
        categorias = []
        for linea in archivo.readlines():
            esp = linea.replace("\n", "").split(", ")
            esp.pop(0)
            for cat in esp:
                if cat not in categorias:
                    categorias.append(cat)
        archivo.close()
        for n in categorias:
            print(n)


llenar = CrearNeo4j()
llenar.caracteristicas()
llenar.close()


