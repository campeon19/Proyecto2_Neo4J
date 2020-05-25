from Conexion import Conexion


class CrearNeo4j:

    """Constructor de la clase"""
    def __init__(self):
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Proyecto123")

    """Funcion para leer el txt y retorna las lineas"""
    def leerTxt(self):
        archivo = open("BasedeDatos.txt", mode="r", encoding="utf-8")
        lineas = []
        for linea in archivo.readlines():
            lineas.append(linea.replace("\n", ""))
        archivo.close()
        return lineas

    """Funcion para llenar la base de datos en relacion a los datos del txt"""
    def fillBase(self):
        data = []
        juegos = self.leerTxt()
        for juego in juegos:
            split = juego.split(", ")
            nombre = split.pop(0)#.replace(" ", "_")
            tags = []
            for n in range(len(split)):
                tags.append(split[n].lower())
            self.conexion.createNode(nombre, tags)
            dic = {"nombre": nombre, "tags": tags}
            data.append(dic)
        for juego in data:
            for tag in juego["tags"]:
                self.conexion.createRelation(juego["nombre"], tag)

    """Funcion para cerrar la conexion con la base de datos"""
    def close(self):
        self.conexion.close()

    """imprime las caracteristicas de los juegos en el txt"""
    def caracteristicas(self):
        archivo = open("BasedeDatos.txt", mode="r", encoding="utf-8")
        categorias = []
        for linea in archivo.readlines():
            esp = linea.replace("\n", "").split(", ")
            esp.pop(0)
            for cat in esp:
                if cat not in categorias:
                    categorias.append(cat.lower())

        archivo.close()
        for n in categorias:
            print(n)


llenar = CrearNeo4j()
llenar.fillBase()
# llenar.caracteristicas()
llenar.close()
