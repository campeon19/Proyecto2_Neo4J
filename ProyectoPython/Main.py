from Controller import Controller
from Conexion import Conexion


class Main:

    """Constructor de la clase"""
    def __init__(self):
        self.controlador = Controller()
        self.controlador.menu()
        #self.conexion = Conexion("bolt://localhost:11003", "neo4j", "Proyecto123")
        #self.conexion.recomendaciones_juego("Assassins Creed Origins")
        #self.conexion.close()
Main()