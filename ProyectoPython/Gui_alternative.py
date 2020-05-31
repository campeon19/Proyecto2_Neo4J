from tkinter import *
from Conexion import Conexion
from tkinter import ttk

# raiz de la interfaz grafica
root = Tk()




#-----------------------------------------------------------------------------------------------------------------------------
#CAMBIAR PARA CADA BASE DE DATOS
root.conexion=Conexion("bolt://localhost:7687", "neo4j", "Bruhxd")
#-----------------------------------------------------------------------------------------------------------------------------

#Aqui se establece el titulo de el juego
root.title("GameRecommend")
root.iconbitmap("recomendation_logo.ico")

#Frame y propiedades
programFrame = Frame(root,width="400",height="600" )
programFrame.pack(fill="both",expand="True")
programFrame.config(cursor="pirate")
programFrame.config(bg = "#ffffff")


#Funcion que se manda a llamar con el boton asociado
def clicked():
    resultado = root.conexion.recomendaciones_juego(EntryTextJuego.get(),SpinnerMinimo.get(),SpinnerMaximo.get(),str(SeleccionConsola.get()))
    indiceJuegos = 1
    textoRecomendacion=""

    #progra defensiva por si meten algo que no existe o si no encuetra recomendaciones
    if len(resultado) > 0:
        for n in resultado:
            textoRecomendacion+="\n"+str(indiceJuegos)+") "+str(n)
            indiceJuegos+=1
    else:
        textoRecomendacion="¡Vaya!\n ¡No se han encontrado \nrecomendaciones para los\n parametros dados!"

   #Se establece el textbox dependiendo de los campos que se pusieron

    # Se habilita para poder escribir
    TextRecommendation.config(state = "normal")
    # Se hace la insersion
    TextRecommendation.delete(1.0,END)
    TextRecommendation.insert(INSERT,textoRecomendacion)
    TextRecommendation.config(state="disabled")



#BOTON
b = Button(programFrame, text="Obtener Recomendacion", font = ('Sans','10','bold'),command=clicked)
imagetest = PhotoImage(file="image_control.png")
b.config(image = imagetest,compound = BOTTOM)
b.place(x=125,y=250)
b.config(bg = "#e3f2fd")

#TEXTBOX de el resultado
TextRecommendation =Text(programFrame,height=10,width=30)
TextRecommendation.place(x=90,y=420)
TextRecommendation.config(state ="disable")
#COLOR TEXTBOX
TextRecommendation.config(bg="#b1bfca")

#label que va arriba en el inicio
LabelTitulo = Label(programFrame,text=str("Sistema de recomendacion de juegos LITE"),font=("Arial","12","bold"))
LabelTitulo.place(x=50,y=0)

#COLOR TITULO
LabelTitulo.config(bg = "#ffffff")

#campo para el juego favorito
LabelJuego = Label(programFrame, text=str("Ingrese su juego favorito"))
LabelJuego.place(x=50,y=50)

#COLOR LABEL JUEGO
LabelJuego.config(bg = "#ffffff")


EntryTextJuego = Entry(programFrame)
EntryTextJuego.place(x=50,y=100)
EntryTextJuego.config(bg="#b1bfca")




#campo para la plataforma en la que juega el usuario
LabelConsola = Label(programFrame, text=str("Ingrese la platataforma \nen la que juega"))
LabelConsola.place(x=250,y=50)

#COLOR LABEL CONSOLA
LabelConsola.config(bg = "#ffffff")


#Configuracion para el combobox

#Variable asociada con el combobox
SeleccionConsola = StringVar()

#combobox de consola
ComboboxConsola = ttk.Combobox(width=20,textvariable=SeleccionConsola)
ComboboxConsola['values']=("PS4","Xbox One","PC","Smartphone","Xbox 360","Wii","Switch","PS3")
ComboboxConsola.place(x=250,y=100)



#Spinner para las horas minimas que juega el usuario
LabelHorasMin = Label(programFrame, text=str("Ingrese las horas minimas \nque juga a la semana"))
LabelHorasMin.place(x=50,y=150)

#COLOR LABEL HORAS MINIMAS
LabelHorasMin.config(bg = "#ffffff")

#SPINNER MINIMO
SpinnerMinimo = Spinbox(programFrame,from_=1,to=12)
SpinnerMinimo.place(x=50,y=200)
#COLOR SPINNER MINIMO
SpinnerMinimo.config(bg="#b1bfca")

#Spinner para las horas maximas que juega el usuario
LabelHorasMax = Label(programFrame, text=str("Ingrese las horas MAXIMAS\n que juga a la semana"))
LabelHorasMax.place(x=250,y=150)

#COLOR LABEL DE HORAS MAXIMAS
LabelHorasMax.config(bg = "#ffffff")

#SPINNER MAXIMO
SpinnerMaximo = Spinbox(programFrame,from_=1,to=12)
SpinnerMaximo.place(x=250,y=200)
#COLOR SPINNER MAXIMO
SpinnerMaximo.config(bg="#b1bfca")

#loop de repeticion para actualizar la vista
root.mainloop()