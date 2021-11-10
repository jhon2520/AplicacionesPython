from tkinter import *

#crear ventana, el método mainloop siempre debe estar al final

raiz = Tk()

miNombre = StringVar()


raiz.title("Titulo de la ventana")
#impedir sizable
raiz.resizable(True,True)
#cambiar icono
raiz.iconbitmap(r"C:\Users\Jhon Romero\Documents\Code++\python\Bots\raven.ico")
#cambiar tamaño
raiz.geometry("650x350")
#cambiar color de fondo
raiz.config(bg="blue")
#cuando trato de ejecutar el archivo sólo este se va a ejecutar con la consola detrás. para que esto no pase
#se debe cambiar la extensión del archivo a pyw

#crear frame y meterlo dentro de la raiz. Todas los metodos de un frame son aplicables a la raiz
miFrame = Frame()
#empaquetarlo es ponerlo dentro del contenedor. mirar la documentación para entender bien esto
# miFrame.pack(side="left",anchor="n")
miFrame.pack(fill="both", expand=True)
#cambiar border
# miFrame.config(border=35)
# miFrame.config(relief="sunken")
#cambiar cursos
# miFrame.config(cursor="pirate")
# como la raiz se adapta al tamño de los frame, la raiz no debe tener nada en el método geometry
miFrame.config(bg="gray",width=550,height=250)

#crear label
miLabel = Label(miFrame,text="pepepeep",foreground="red",font=("poppins", 18))
miLabel.pack()
#ubicar label
miLabel.place(x=0,y=250)
#Usar imagen como label. deben ser png o gif
# miImagen = PhotoImage(file="raven.png")
# milabel2 = Label(miFrame, image=miImagen,width=120,height=120)
# milabel2.pack()

#crear textbox llamados Entry
# miEntry = Entry(miFrame)
# miEntry.pack()
# miEntry.place(x=0,y=0)

#crear label con tbx usando el método grid
#alinear label con el método sticky N NE E SE  S SW W
#usar padding padx o pady
miEntry = Entry(miFrame)
miEntry.pack()
#coloca elementos en casillas desde la fila y columna 0
miEntry.grid(row=0,column=1)
nombre = Label(miFrame,text="nombre")
nombre.grid(row=0,column=0,sticky="w",pady=5)


labelApellido = Label(miFrame,text="insete su apellido")
labelApellido.grid(row=1,column=0)
cuadroApellido = Entry(miFrame)
cuadroApellido.config(foreground="red",justify="center",textvariable=miNombre)
cuadroApellido.grid(row=1,column=1,sticky="w",padx=5, pady=5)


#contraseña
labelContra = Label(miFrame,text="inserte contraseña")
labelContra.grid(row=2,column=0)
cuadroContra = Entry(miFrame)
cuadroContra.config(show="*")
cuadroContra.grid(row=2,column=1)

#Crear richtextBox, este es por defecto bastante grande, la barra de scroll se debe colocar manualmente
labelComentario = Label(miFrame,text="Deje sus comentarios")
labelComentario.grid(row=3,column=0)
textoComentario = Text(miFrame,width=16,height=12)
textoComentario.grid(row=3,column=1)
    #crear scroll dicíendole a quien pertenece y que funciona de manera vertical, la ubicación debe ser una columna o fila más, también
    #se debe modificar su tamaño = nsew. también se debe agregar el comportamiento automático
scrollVert = Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=3,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

def codigoBtn():
    #dar valor a tbx -> Set. #obtener valor  ->get
    miNombre.set("Jhon")

#Crear Btn
BotonEnvio = Button(miFrame,text="Enviar",command=codigoBtn)
BotonEnvio.grid(row=4,column=5)




raiz.mainloop()