from os import pardir
from tkinter import *
from PIL import ImageTk,Image

colorFondo = "#fff"
colorFrame = "#ffe"
suma = 0
valor = 2


#base
root = Tk()
valor = StringVar()
root.title("Calculdora")
root.resizable(False,False)
root.iconbitmap(r"C:/Users/Jhon Romero/Documents/Code++/python/Bots/raven.ico")
root.geometry("425x430")

#Crear frame
backFrame = Frame()
backFrame.config(bg=colorFrame,width=600,height=700,pady=30,padx=20)
backFrame.pack(fill="both",expand=True)

#crear imagen
    #resize img usando librería PIL
logoImg = Image.open("C:/Users/Jhon Romero/Documents/Code++/python/Bots/raven.png")
resized = logoImg.resize((60,60), Image.ANTIALIAS)
newImgLogo = ImageTk.PhotoImage(resized)
labelImg = Label(backFrame,image=newImgLogo,background=colorFrame)
labelImg.grid(row=0,column=0)

#crear Label
labelSuperior = Label(backFrame,text="Dato ingresado",background=colorFrame)
labelSuperior.grid(row=0,column=1,sticky=W)

#Crear tbx de ingreso de datos
frameHeader = Frame(backFrame)
frameHeader.grid(row=0,column=2,columnspan=2)
frameHeader.config(bg="white",width=650,height=60,pady=20,padx=20)
tbxDato = Entry(frameHeader,textvariable=valor)
tbxDato.grid(row=0,column=0)

#setvalue
def btn_click(number):
    #tbxDato.get() obtiene el valor actual del objeto
    # tbxDato.delete(0,END)
    tbxDato.insert(END,number)
    valor = tbxDato.get()
    

def btn_clear():
    tbxDato.delete(0,END)

def btn_sumar():
    primer_numero = tbxDato.get()
    global f_number
    f_number = int(primer_numero)
    tbxDato.delete(0,END)
    global operacion
    operacion = 1

def btn_restar():
    primer_numero = tbxDato.get()
    global f_number
    f_number = int(primer_numero)
    tbxDato.delete(0,END)
    global operacion
    operacion = 0


# def btn_mult():
#     primer_numero = tbxDato.get()
#     global f_number
#     f_number = primer_numero
#     tbxDato.delete(0, END)
#     global operacion
#     operacion = 'mult'

# def btn_igual():
#     segundo_numero = tbxDato.get()
#     tbxDato.delete(0, END)
#     multiplicacion = int(f_number) * int(segundo_numero)
#     tbxDato.insert(0, multiplicacion)

def btn_igual():
    second_number = tbxDato.get()
    tbxDato.delete(0,END)

    if operacion == 1:
        tbxDato.insert(0,f_number + int(second_number))
    if operacion == 0:
        tbxDato.insert(0,f_number - int(second_number))

#CrearBotones
btn0 = Button(backFrame,text="0",padx=40,pady=20, command=lambda: btn_click(0),background=colorFondo)
btn1 = Button(backFrame,text="1",padx=40,pady=20,command=lambda: btn_click(1),background=colorFondo)
btn2 = Button(backFrame,text="2",padx=40,pady=20,command=lambda: btn_click(2),background=colorFondo)
btn3 = Button(backFrame,text="3",padx=40,pady=20,command=lambda: btn_click(3),background=colorFondo)
btn4 = Button(backFrame,text="4",padx=40,pady=20,command=lambda: btn_click(4),background=colorFondo)
btn5 = Button(backFrame,text="5",padx=40,pady=20,command=lambda: btn_click(5),background=colorFondo)
btn6 = Button(backFrame,text="6",padx=40,pady=20,command=lambda: btn_click(6),background=colorFondo)
btn7 = Button(backFrame,text="7",padx=40,pady=20,command=lambda: btn_click(7),background=colorFondo)
btn8 = Button(backFrame,text="8",padx=40,pady=20,command=lambda: btn_click(8),background=colorFondo)
btn9 = Button(backFrame,text="9",padx=40,pady=20,command=lambda: btn_click(9),background=colorFondo)
btnSumar = Button(backFrame,text="+",padx=38,pady=52,command=btn_sumar,background=colorFondo)
btnRestar = Button(backFrame,text="-",padx=40,pady=20,command=btn_restar,background=colorFondo)
btnMult = Button(backFrame,text="*",padx=39,pady=20,command=btn_click,background=colorFondo)
btnDiv = Button(backFrame,text="/",padx=40,pady=20,command=btn_click,background=colorFondo)
btnClear = Button(backFrame,text="C",padx=40,pady=20,command=btn_clear,background=colorFondo)
btnEqual = Button(backFrame,text="=",padx=182,pady=20,command=btn_igual,background=colorFondo)

#ubicar Botones

btn0.grid(row=5,column=0)
btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btnMult.grid(row=2,column=3)
btnSumar.grid(row=3,column=3,rowspan=2)
btnRestar.grid(row=5,column=3)
btnDiv.grid(row=5,column=2)
btnClear.grid(row=5,column=1)
btnEqual.grid(row=6,column=0,columnspan=4)




root.mainloop()