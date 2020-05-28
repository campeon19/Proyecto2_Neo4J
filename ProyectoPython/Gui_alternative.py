from tkinter import*


root = Tk()
root.title("GameRecommend System")
#para bloquear pantalla: root.resizeable(0,0)

#coloca el icono de la ventana
root.iconbitmap("recomendation_logo.ico")

#largo de la ventana
#root.geometry("650x350")

programFrame = Frame(root,width="650",height="350" )
#programFrame.pack(side="left",anchor="n")

programFrame.pack(fill="both",expand="True")
#programFrame.config(bg = "#ffffff") #el color se da en hexadecimal

#programFrame.config(width="650",height="350")

#este es para el mouse, si quieren lo pueden quitar
programFrame.config(cursor="pirate")

titleLabel = Label(programFrame,text ="HolaMundo",font=("Arial","18"))
titleLabel.place(x=300,y=0)

numero: int = 1


entryText = Entry(programFrame)
entryText.place(x=300,y=300)


def helloCallBack():

    titleLabel.config(text=numero)
    ++numero

#programFrame.config(relief="groove")


B = Button(programFrame, text ="Hello", command = helloCallBack)
B.place(x=300,y=350)


root.mainloop()


