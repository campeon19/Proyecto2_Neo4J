from Controller import Controller

def Interfaz():
    print("----- Bienvenido al sistema de recomendaciones -----")

class Main:

    """Constructor de la clase"""
    def __init__(self):
        Interfaz()
        self.controlador = Controller()




Main()