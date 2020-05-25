from Conexion import Conexion

class Controller:

    def __init__(self):
        self.conexion = Conexion("bolt://localhost:7687", "neo4j", "Proyecto123")
        self.conexion.createNode("Call of Duty 1", ["accion", "aventura", "shooter"])
        #self.conexion.deleteNode("Call_of_Duty")
        self.conexion.close()


Controller()
