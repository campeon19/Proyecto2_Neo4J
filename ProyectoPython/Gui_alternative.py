from tkinter import*
root = Tk()
root.title("GameRecommend System")
#para bloquear pantalla: root.resizeable(0,0)

#coloca el icono de la ventana
root.iconbitmap("recomendation_logo.ico")

#largo de la ventana
#root.geometry("650x350")

programFrame = Frame()
#programFrame.pack(side="left",anchor="n")
programFrame.pack(fill="both",expand="True")
programFrame.config(bg = "#ffffff") #el color se da en hexadecimal

programFrame.config(width="650",height="350")

#este es para el mouse, si quieren lo pueden quitar
programFrame.config(cursor="pirate")

#programFrame.config(relief="groove")


root.mainloop()


