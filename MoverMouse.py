import time
from tkinter import font
import pyautogui as pg
import sched
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import threading
import os
import sys


colorFrame = "#FEF5ED"
colorBtns = "#2F86A6"
blanco = "#fff"
lblFontColor = "#345B63"
pg.FAILSAFE = False

nombre_app = "MoverMouse.py"

if getattr(sys,"frozen",False):
    ruta = os.path.dirname(sys.executable)
elif __file__:
    ruta = os.path.dirname(__file__)

ruta_completa = os.path.join(ruta,nombre_app)


#base
root = Tk()

    #center screen
w = 640
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.title("Controlador de Inactividad 1.1")
root.resizable(False,False)
root.iconbitmap(ruta + r"\raven.ico")
# root.geometry("640x300")
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
lblFont = font.Font(family="poppins",size=12)


#Crear Frame
backFrame = Frame()
backFrame.config(bg=colorFrame,width=600,height=700,pady=30,padx=20)
backFrame.pack(fill="both",expand=True)

#label superior
lblSuperior = Label(backFrame,text="Bienvenido al controlador de inactividad automático \n seleccione cuántos minutos desea controlar\n ",background=colorFrame,fg=lblFontColor)
lblSuperior.grid(row=0, column= 1,columnspan=6)
lblSuperior["font"] = lblFont

#lbl Indicador
lblIndicador = Label(backFrame,text="",background=colorFrame,fg=colorBtns)
lblIndicador.grid(row=1,column=2,columnspan=3)
lblIndicador["font"] = lblFont

#label para espacio
lblVacia = Label(backFrame,text="\n\n\n")
lblVacia.grid(row=1,column=0)
lblVacia2 = lblVacia
lblVacia2.grid(row=2,column=0)

#lbl estado
lblEstado = Label(backFrame,text="Estado:",background=colorFrame,fg= lblFontColor,pady=20)
lblEstado.grid(row=5,column=0,sticky="e")
#lbl estado Valor
lblEstadoValor = Label(backFrame,text="Inactivo",background=colorFrame,fg= "#911F27",pady=20)
lblEstadoValor.grid(row=5,column=1,sticky="w")

#lbl Nombre
lblNombre = Label(backFrame,text="Jhon Romero",background=colorFrame,fg= lblFontColor)
lblNombre.grid(row=5,column=5,rowspan=2)
lblNombre["font"] = font.Font(family="poppins",size=7)

#crear imagen
    #resize img usando librería PIL
logoImg = Image.open(ruta + r"\raven.png")
resized = logoImg.resize((80,80), Image.ANTIALIAS)
newImgLogo = ImageTk.PhotoImage(resized)
labelImg = Label(backFrame,image=newImgLogo,background=colorFrame)
labelImg.grid(row=0,column=0)

#Metodos
global minutos
minutos = 0

def btn_hover_enter(e):
    e.widget["background"] = "#345B63"
    # e.widget["font"] = font.Font( family="poppins" )
def btn_hover_leave(e):
    e.widget["background"] = "#2F86A6"
    # e.widget["font"] = font.Font( family="poppins")

def btn1_press():
    lblIndicador.config(text="Controlar: 1 minuto")
    global minutos
    minutos = 1
def btn5_press():
    lblIndicador.config(text="Controlar: 5 minutos")
    global minutos
    minutos = 5
def btn10_press():
    lblIndicador.config(text="Controlar: 10 minutos")
    global minutos
    minutos = 10
def btn20_press():
    lblIndicador.config(text="Controlar: 20 minutos")
    global minutos
    minutos = 20
def btn60_press():
    lblIndicador.config(text="Controlar: 60 minutos")
    global minutos
    minutos = 60
def btn120_press():
    lblIndicador.config(text="Controlar: 120 minutos")
    global minutos
    minutos = 120


s = sched.scheduler(time.time, time.sleep)
mousex = 0
mousey = 0

def btn_aceptar():
    try:
        lblEstadoValor.config(text="Activo",fg= lblFontColor)
        global continuar
        continuar = True
        global segundos 
        segundos =  minutos * 60

        if segundos == 0:
            segundos = 10
            lblIndicador.config(text="Valor por defecto: 10 seg")

        cambiar_estado_btn()
        root.iconify()

        while continuar:
            s.enter(0, 1, mover_mouse, (s,))
            s.run()

    except Exception as inst:
        messagebox.showerror(title="Error", message= "error: " + str(inst))


# def btn_cancelar():

    # lblEstadoValor.config(text="Inactivo",fg= "#911F27")
    # lblIndicador.config(text="")
    # global minutos
    # minutos = 0
    # global continuar
    # continuar = False
    # cambiar_estado_btn()



    
def cambiar_estado_btn():
    if btnAceptar["state"] == "normal":
        btnAceptar["state"] = "disabled"
        btnAceptar["text"] = "Aceptar"
    else:
        btnAceptar["state"] = "normal"
        btnAceptar["text"] = "Aceptar"


def on_closing():
        if messagebox.askokcancel("SALIR", "¿Desea salir de la aplicación?"):
            #Eliminar todos los hilos creados 
            os._exit(1)

root.protocol("WM_DELETE_WINDOW",on_closing)

def mover_mouse(sc): 
    mousex,mousey = pg.position()
    # print("segundos a esperar: " + str(segundos))
    time.sleep(segundos)
    mousex2,mousey2 = pg.position()

    if((mousex == mousex2) and (mousey == mousey2)):
        pg.moveRel(10,0)
        pg.press(["up"])
        s.enter(0, 1, mover_mouse, (sc,))
        pg.moveRel(-10,0)
        pg.press(["down"])
    
def btn_aceptar_lambda():

    global hilo
    hilo = threading.Thread(target=btn_aceptar)
    hilo.daemon = True
    hilo.start()




#crear botones

btn1 = Button(backFrame,text="1",padx=40,pady=4,command=btn1_press,background=colorBtns, fg=blanco,font=font.Font(family="poppins",size=9))
btn5 = Button(backFrame,text="5",padx=40,pady=4,command=btn5_press,background=colorBtns,fg=blanco,font=font.Font(family="poppins",size=9))
btn10 = Button(backFrame,text="10",padx=40,pady=4,command=btn10_press,background=colorBtns,fg=blanco,font=font.Font(family="poppins",size=9))
btn20= Button(backFrame,text="20",padx=40,pady=4,command=btn20_press,background=colorBtns,fg=blanco,font=font.Font(family="poppins",size=9))
btn60 = Button(backFrame,text="60",padx=40,pady=4,command=btn60_press,background=colorBtns,fg=blanco,font=font.Font(family="poppins",size=9))
btn120 = Button(backFrame,text="120",padx=40,pady=4,command=btn120_press,background=colorBtns,fg=blanco,font=font.Font(family="poppins",size=9))
btnAceptar = Button(backFrame,text="Aceptar",padx=73,pady=1,command=btn_aceptar_lambda,background=lblFontColor,fg=blanco,font=font.Font(family="poppins",size=8))
# btnCancelar = Button(backFrame,text="Cancelar",padx=73,pady=1,command=btn_cancelar,background="#911F27",fg=blanco,font=font.Font(family="poppins",size=8))
# btnPrueba = Button(backFrame,text="prueba",command=prueba)

# command=lambda: threading.Thread(target=btn_aceptar).start()


btn1.bind("<Enter>",btn_hover_enter)
btn1.bind("<Leave>",btn_hover_leave)
btn5.bind("<Enter>",btn_hover_enter)
btn5.bind("<Leave>",btn_hover_leave)
btn10.bind("<Enter>",btn_hover_enter)
btn10.bind("<Leave>",btn_hover_leave)
btn20.bind("<Enter>",btn_hover_enter)
btn20.bind("<Leave>",btn_hover_leave)
btn60.bind("<Enter>",btn_hover_enter)
btn60.bind("<Leave>",btn_hover_leave)
btn120.bind("<Enter>",btn_hover_enter)
btn120.bind("<Leave>",btn_hover_leave)

btnAceptar.bind("<Leave>",btn_hover_enter)
btnAceptar.bind("<Enter>",btn_hover_leave)


#ubicar botones

btn1.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn10.grid(row=2,column=2)
btn20.grid(row=2,column=3)
btn60.grid(row=2,column=4)
btn120.grid(row=2,column=5)
btnAceptar.grid(row=4,column=2,columnspan=2)
# btnCancelar.grid(row=4,column=3,columnspan=2)
# btnPrueba.grid(row=5,column=0)


