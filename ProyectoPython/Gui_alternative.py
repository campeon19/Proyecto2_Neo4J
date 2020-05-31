from tkinter import *
from Conexion import Conexion

root = Tk()

# variable is stored in the root object
root.counter = 0

root.conexion=Conexion("bolt://localhost:7687", "neo4j", "Bruhxd")
root.title("GameRecommend")
root.iconbitmap("recomendation_logo.ico")
programFrame = Frame(root,width="750",height="600" )
programFrame.pack(fill="both",expand="True")
programFrame.config(cursor="pirate")

def clicked():
    root.counter += 1
    resultado = root.conexion.recomendaciones_juego(EntryTextJuego.get(),SpinnerMinimo.get(),SpinnerMaximo.get(),EntryTextConsola.get())
    indiceJuegos = 1
    textoRecomendacion=""
    if len(resultado) > 0:
        for n in resultado:
            textoRecomendacion+="\n"+str(indiceJuegos)+") "+str(n)
            indiceJuegos+=1
    else:
        textoRecomendacion="Vaya!\n no se han encontrado recomendaciones para los parametros dados"

    #L['text'] = textoRecomendacion
    TextRecommendation.config(state = "normal")
    TextRecommendation.delete(1.0,END)
    TextRecommendation.insert(INSERT,textoRecomendacion)
    TextRecommendation.config(state="disabled")
    #aqui se debe de poner lo que va a ir en el texto



b = Button(programFrame, text="Obtener Recomendacion", command=clicked)
b.place(x=150,y=250)


#texto que dara las recomendaciones
#L = Label(programFrame, text=str("No hay recomendaciones"))
#L.place(x=300,y=350)
TextRecommendation =Text(programFrame,height=10,width=30)
TextRecommendation.place(x=50,y=350)
TextRecommendation.config(state ="disable")

#label que va arriba en el inicio
LabelTitulo = Label(programFrame,text=str("Sistema de recomendacion de juegos LITE"),font=("Arial","12","bold"))
LabelTitulo.place(x=200,y=0)

#campo para el juego favorito
LabelJuego = Label(programFrame, text=str("Ingrese su juego favorito"))
LabelJuego.place(x=50,y=50)

EntryTextJuego = Entry(programFrame)
EntryTextJuego.place(x=50,y=100)


#campo para la plataforma en la que juega el usuario
LabelConsola = Label(programFrame, text=str("Ingrese la platataforma \nen la que juega"))
LabelConsola.place(x=250,y=50)

EntryTextConsola = Entry(programFrame)
EntryTextConsola.place(x=250,y=100)


#Spinner para las horas minimas que juega el usuario
LabelHorasMin = Label(programFrame, text=str("Ingrese las horas minimas \nque juga a la semana"))
LabelHorasMin.place(x=50,y=150)

SpinnerMinimo = Spinbox(programFrame,from_=1,to=12)
SpinnerMinimo.place(x=50,y=200)

#Spinner para las horas maximas que juega el usuario
LabelHorasMax = Label(programFrame, text=str("Ingrese las horas MAXIMAS\n que juga a la semana"))
LabelHorasMax.place(x=250,y=150)

SpinnerMaximo = Spinbox(programFrame,from_=1,to=12)
SpinnerMaximo.place(x=250,y=200)

root.mainloop()