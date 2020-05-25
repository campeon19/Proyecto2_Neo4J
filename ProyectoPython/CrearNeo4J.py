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




llenar = CrearNeo4j()
llenar.fillBase()
llenar.close()


