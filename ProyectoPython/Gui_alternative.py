from tkinter import *
from Conexion import Conexion

root = Tk()

# variable is stored in the root object
root.counter = 0
root.conexion=Conexion("bolt://localhost:7687", "neo4j", "Bruhxd")
programFrame = Frame(root,width="750",height="600" )
programFrame.pack(fill="both",expand="True")
programFrame.config(cursor="pirate")

def clicked():
    root.counter += 1
    resultado = root.conexion.recomendaciones_juego("Rocket League",1,3,"PS4")
    indiceJuegos = 1
    textoRecomendacion=""
    if len(resultado) > 0:
        for n in resultado:
            textoRecomendacion+="\n"+str(indiceJuegos)+") "+str(n)
            indiceJuegos+=1
    else:
        textoRecomendacion="Vaya!\n no se han encontrado recomendaciones para los parametros dados"

    L['text'] = textoRecomendacion


b = Button(programFrame, text="Obtener Recomendacion", command=clicked)
b.place(x=300,y=300)

L = Label(programFrame, text=str("No hay recomendaciones"))
L.place(x=300,y=350)

LabelTitulo = Label(programFrame,text=str("Sistema de recomendacion de juegos LITE"),font=("Arial","12","bold"))
LabelTitulo.place(x=200,y=0)

#campo para el juego favorito
LabelJuego = Label(programFrame, text=str("Ingrese su juego favorito"))
LabelJuego.place(x=50,y=50)

EntryTextJuego = Entry(programFrame)
EntryTextJuego.place(x=75,y=100)


#campo para la plataforma en la que juega el usuario
LabelConsola = Label(programFrame, text=str("Ingrese la platataforma en la que juega"))
LabelConsola.place(x=450,y=50)

EntryTextConsola = Entry(programFrame)
EntryTextConsola.place(x=475,y=100)


#Spinner para las horas minimas que juega el usuario
LabelHorasMin = Label(programFrame, text=str("Ingrese las horas minimas \nque juga a la semana"))
LabelHorasMin.place(x=50,y=150)

SpinnerMinimo = Spinbox(programFrame,from_=1,to=12)
SpinnerMinimo.place(x=50,y=200)

#Spinner para las horas maximas que juega el usuario
LabelHorasMax = Label(programFrame, text=str("Ingrese las horas MAXIMAS que juga a la semana"))
LabelHorasMax.place(x=450,y=150)

SpinnerMaximo = Spinbox(programFrame,from_=1,to=12)
SpinnerMaximo.place(x=450,y=200)

root.mainloop()