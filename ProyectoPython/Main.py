from Controller import Controller


class Main:

    """Constructor de la clase"""
    def __init__(self):
        self.controlador = Controller()
        self.controlador.menu()
        #self.controlador.searchTimeTags(["deportes", "estrategia", "star wars"], "0", "5")
        #print(self.controlador.getCharacteristics())
        #self.controlador.close()
Main()