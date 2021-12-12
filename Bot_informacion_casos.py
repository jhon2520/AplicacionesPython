from tkinter import *
import time
from PIL.ImageOps import grayscale
import pyautogui as pg 
import sys
import os
from tkinter import font

#Base
nombre_app = "Bot_informacion_casos.py"
lblFontColor = "#345B63"
colorFrame = "#FEF5ED"

if getattr(sys,"frozen",False):
    ruta = os.path.dirname(sys.executable)
elif __file__:
    ruta = os.path.dirname(__file__)

ruta_completa = os.path.join(ruta,nombre_app)


root = Tk()
segundos = 1
lblFont = font.Font(family="poppins",size=8)
w = 660
h = 460
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.title("Bot de información - ASOCEBU")
root.resizable(False,False)
root.iconbitmap(ruta + r"\raven.ico")
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def btn_hover_enter(e):
    e.widget["background"] = "#2F86A6"
def btn_hover_leave(e):
    e.widget["background"] = "#345B63"

    

#Crear Frame
backFrame = Frame()
backFrame.config(bg=colorFrame,width=600,height=700,pady=30,padx=20)
backFrame.pack(fill="both",expand=True)

#label superior
lblSuperior = Label(backFrame,text="Bienvenido al Bot  \n Siga los siguientes pasos para el correcto funcionamiento.\n ",background=colorFrame,fg=lblFontColor)
lblSuperior.grid(row=0, column= 0,columnspan=6)
lblSuperior["font"] = lblFontColor

#label para espacio
lblVacia = Label(backFrame,text="\n")
lblVacia.grid(row=1,column=0)
lblVacia2 = lblVacia
lblVacia2.grid(row=2,column=0)

#indicaciones
lblIndicaciones = Label(backFrame,text="1. Debe tener el navegador Chrome instalado. \n2. Disponga de un computador eficiente. \n3. Debe tener abiertos la hoja de excel donde se encuentran los datos en la ventana siguiente a este progama. \n4. La hoja de excel debe tener los valor a buscar en la columna A y libre las siguientes 5 columnas. \n5. Si su computador es lento, seleccione más segundos por proceso; el valor por defecto es 1 segundo. \n6. El bot busca información completa, cada registro debe tener mínimo los 7 caracteres \n7. No debe haber registros en blanco o valores inválidos \n8.El bot funciona a través del reconocimiento de imágnes por lo que puede ser necesario capturarlas \nnuevamente al ejecutarse por primera vez.",justify=LEFT, background=colorFrame,fg=lblFontColor)
lblIndicaciones["font"] = lblFont
lblIndicaciones.grid(row=3,column=0, columnspan=2)

lblVacia3 = lblVacia
lblVacia3.grid(row=4,column=1)
lblVacia4 = lblVacia
lblVacia4.grid(row=5,column=1)

#input segundos
tbxSegundos = Entry(backFrame,justify=CENTER)
tbxSegundos.grid(row=6,column=0)
labelSegundos = Label(backFrame,text="Cantidad de degundos", background=colorFrame,fg=lblFontColor)
labelSegundos.grid(row=7,column=0)

#input cantidad registros
tbxRegistros = Entry(backFrame,justify=CENTER)
tbxRegistros.grid(row=6,column=1)
labelSegundos = Label(backFrame,text="Cantidad de registros", background=colorFrame,fg=lblFontColor)
labelSegundos.grid(row=7,column=1)

lblVacia5 = Label(backFrame,text="\n")
lblVacia5.grid(row=8,column=0 )


def btn_aceptar():

    tbxValueSeg = tbxSegundos.get()
    tbxValueRegistros = tbxRegistros.get()

    if (tbxValueSeg.isnumeric() == True and tbxValueRegistros.isnumeric() == True):
        global segundos
        segundos = int(tbxValueSeg)
        global registros
        registros = int(tbxValueRegistros)
        print(segundos+1)
        root.iconify()
    else:
        pg.alert("El valor ingresado no corresponde a un valor correcto. \nIngrese solo valores númericos enteros")
    
    

#btn
btnAceptar = Button(backFrame,command=btn_aceptar, text="Iniciar Bot",padx=10,pady=6,background=lblFontColor,fg="#fff")
btnAceptar.grid(row=9 ,column=0,columnspan=2)
btnAceptar.bind("<Enter>",btn_hover_enter)
btnAceptar.bind("<Leave>",btn_hover_leave)





root.mainloop()

# pg.alert("Iniciando código")



# colores = [' let c = document.getElementById("cphMostrarPaginas_lblColorAnimal")','let vC = c.innerText','copy(vC)']
# nacimientos = ['let f = document.getElementById("cphMostrarPaginas_lblFecNacimiento")','let vF = f.innerText','copy(vF)']
# padres = [" let p = document.getElementById('cphMostrarPaginas_lblNumeroPadre')"," let vP = p.innerText"," copy(vP)"]
# madres = [" let m = document.getElementById('cphMostrarPaginas_lblNumeroMadre')"," let vM = m.innerText"," copy(vM)"]
# propietarios = [" let pr = document.getElementById('cphMostrarPaginas_lblNombrePropietario')"," let nPr = pr.innerText"," copy(nPr)"]


# descargar_PDF1 = "let descargarPDF = document.getElementById('cphMostrarPaginas_btnImprimir')"
# descargar_PDF2 = "descargarPDF.click()"


# def mover_vertical():
#     pg.press("down")

# def mover_horizontal():
#     pg.press("right")

# def retornar_columna1():
#     pg.hotkey("ctrl","left")

# def copiar_celda():
#     pg.hotkey("ctrl","c")

# def abrir_chrome():
#     pg.hotkey("ctrl","c")
#     pg.hotkey("win","s")
#     pg.write("chrome")
#     time.sleep(1)
#     pg.press("enter")
#     time.sleep(1)
#     pg.write("https://www.asocebu.com/index.php/blog/registros")
#     pg.press("enter")

# def abrir_consola():
#     pg.hotkey("shift","ctrl","j")
#     time.sleep(2)

# def maximizar_ventana():
#     pg.hotkey("win","up")

# def pegar_valor():
#     pg.hotkey("ctrl","v")

# def press_enter():
#     pg.press("enter")

# def continuar():
#     continuar_bool = False
#     while not continuar_bool:
#         btn = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\imagenes_bot\btn_consultar.PNG",grayscale=True,confidence=0.8)
#         # print(btn)
#         if btn != None:
#             continuar_bool = True
#             return

# def continuar_presionar_lupa():
#     continuar_bool = False
#     while not continuar_bool:
#         btn = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\imagenes_bot\lupa.PNG",grayscale=True,confidence=0.8)
#         # print(btn)
#         if btn != None:
#             pg.click(btn)
#             continuar_bool = True
#             return


# def continuar_logo_consulta():
#     continuar_bool = False
#     while not continuar_bool:
#         btn = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\imagenes_bot\datos_basicos.PNG",grayscale=True,confidence=0.8)
#         # print(btn)
#         if btn != None:
#             pg.click(btn)
#             pg.click(button="right")
#             pg.press("up")
#             press_enter()
#             continuar_bool = True
#             return


# def presionar_tab(veces):
#     for i in range(veces):
#         pg.press("tab")

# def abrir_consola_en_elementos():
#     pg.hotkey("ctrl","]")

# def retornar_y_pegar():
#     pg.hotkey("alt","tab")
#     time.sleep(1)
#     mover_horizontal()
#     time.sleep(1)
#     pegar_valor()

# def buscador_html(arreglo):
#         pg.hotkey("alt","tab")
#         time.sleep(1)
#         pg.write(arreglo[0])
#         pg.hotkey("shift","enter")
#         pg.write(arreglo[1])
#         pg.hotkey("shift","enter")
#         pg.write(arreglo[2])
#         pg.press("enter")
#         time.sleep(1)
    

# def recargar_pagina():
#     pg.hotkey("shift","ctrl","j")
#     pg.press("f5")


# contadorVertical = 0
# contadorHorizontal = 0

# #cambiar al archivo de excel
# time.sleep(0.5)
# pg.hotkey("alt","tab")
# time.sleep(0.5)



    
# if contadorHorizontal == 0:
#     time.sleep(1)
#     mover_vertical()
#     copiar_celda()
#     time.sleep(1)
#     abrir_chrome()
#     time.sleep(1)
#     continuar()
#     maximizar_ventana()
#     presionar_tab(17)
#     pegar_valor()
#     presionar_tab(3)
#     press_enter()

#     #presionar lupa
#     continuar_presionar_lupa()

#     # dibujar html presionando el logo
#     continuar_logo_consulta()
#     time.sleep(1)
#     abrir_consola_en_elementos()
#     time.sleep(1)

    
#     pg.write('let c = document.getElementById("cphMostrarPaginas_lblColorAnimal")')
#     pg.hotkey("shift","enter")
#     pg.write('let vC = c.innerText')
#     pg.hotkey("shift","enter")
#     pg.write('copy(vC)')
#     pg.press("enter")

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar la fecha de nacimiento
#     buscador_html(nacimientos)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar el padre
#     buscador_html(padres)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar la madre
#     buscador_html(madres)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     # #vuelve a la consola a buscar la propietario
#     buscador_html(propietarios)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #descargarPDF
#     pg.hotkey("alt","tab")
#     time.sleep(0.5)
#     pg.write(descargar_PDF1)
#     pg.hotkey("shift","enter")
#     pg.write(descargar_PDF2)
#     press_enter()

#     contadorHorizontal += 1
    

# while contadorHorizontal == 1:
    
#     #mover a siguiente fila
#     pg.hotkey("alt","tab")
#     time.sleep(1)
#     retornar_columna1()
#     mover_vertical()
#     copiar_celda()
#     time.sleep(1)

#     #retornar a la pagina y recargarla
#     pg.hotkey("alt","tab")
#     time.sleep(1)
#     recargar_pagina()
#     time.sleep(1)
#     continuar()
#     time.sleep(1)
#     presionar_tab(17)
#     time.sleep(1)
#     pegar_valor()
#     time.sleep(1)
#     presionar_tab(3)
#     press_enter()

#     #presionar lupa
#     continuar_presionar_lupa()

#     # dibujar html presionando el logo
#     continuar_logo_consulta()
#     time.sleep(1)
#     abrir_consola_en_elementos()
#     time.sleep(1)
#     pg.write('let c = document.getElementById("cphMostrarPaginas_lblColorAnimal")')
#     pg.hotkey("shift","enter")
#     pg.write('let vC = c.innerText')
#     pg.hotkey("shift","enter")
#     pg.write('copy(vC)')
#     pg.press("enter")

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar la fecha de nacimiento
#     buscador_html(nacimientos)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar el padre
#     buscador_html(padres)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar la madre
#     buscador_html(madres)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #vuelve a la consola a buscar la propietario
#     buscador_html(propietarios)

#     #volver al archivo de excel
#     retornar_y_pegar()

#     #descargarPDF
#     pg.hotkey("alt","tab")
#     time.sleep(0.5)
#     pg.write(descargar_PDF1)
#     pg.hotkey("shift","enter")
#     pg.write(descargar_PDF2)
#     press_enter()

