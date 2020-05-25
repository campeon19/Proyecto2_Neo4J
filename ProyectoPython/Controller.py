from Conexion import Conexion

class Controller:

    def __init__(self):
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Proyecto123")
        #self.conexion.createNode("Call of Duty 1", ["first person", "aventura", "shooter"])
        #self.conexion.deleteNode("Call of Duty 1")
        print(self.conexion.searchtags(["aventura"]))
        self.conexion.close()


Controller()
