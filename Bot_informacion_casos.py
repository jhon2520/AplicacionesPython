import time
from PIL.ImageOps import grayscale
import pyautogui as pg 



pg.alert("Iniciando código")



colores = [' let c = document.getElementById("cphMostrarPaginas_lblColorAnimal")','let vC = c.innerText','copy(vC)']
nacimientos = ['let f = document.getElementById("cphMostrarPaginas_lblFecNacimiento")','let vF = f.innerText','copy(vF)']
padres = [" let p = document.getElementById('cphMostrarPaginas_lblNumeroPadre')"," let vP = p.innerText"," copy(vP)"]
madres = [" let m = document.getElementById('cphMostrarPaginas_lblNumeroMadre')"," let vM = m.innerText"," copy(vM)"]
propietarios = [" let pr = document.getElementById('cphMostrarPaginas_lblNombrePropietario')"," let nPr = pr.innerText"," copy(nPr)"]


descargar_PDF1 = "let descargarPDF = document.getElementById('cphMostrarPaginas_btnImprimir')"
descargar_PDF2 = "descargarPDF.click()"


def mover_vertical():
    pg.press("down")

def mover_horizontal():
    pg.press("right")

def retornar_columna1():
    pg.hotkey("ctrl","left")

def copiar_celda():
    pg.hotkey("ctrl","c")

def abrir_chrome():
    pg.hotkey("ctrl","c")
    pg.hotkey("win","s")
    pg.write("chrome")
    time.sleep(1)
    pg.press("enter")
    time.sleep(1)
    pg.write("https://www.asocebu.com/index.php/blog/registros")
    pg.press("enter")

def abrir_consola():
    pg.hotkey("shift","ctrl","j")
    time.sleep(2)

def maximizar_ventana():
    pg.hotkey("win","up")

def pegar_valor():
    pg.hotkey("ctrl","v")

def press_enter():
    pg.press("enter")

def continuar():
    continuar_bool = False
    while not continuar_bool:
        btn = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\imagenes_bot\btn_consultar.PNG",grayscale=True,confidence=0.8)
        # print(btn)
        if btn != None:
            continuar_bool = True
            return

def continuar_presionar_lupa():
    continuar_bool = False
    while not continuar_bool:
        btn = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\imagenes_bot\lupa.PNG",grayscale=True,confidence=0.8)
        # print(btn)
        if btn != None:
            pg.click(btn)
            continuar_bool = True
            return


def continuar_logo_consulta():
    continuar_bool = False
    while not continuar_bool:
        btn = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\imagenes_bot\datos_basicos.PNG",grayscale=True,confidence=0.8)
        # print(btn)
        if btn != None:
            pg.click(btn)
            pg.click(button="right")
            pg.press("up")
            press_enter()
            continuar_bool = True
            return


def presionar_tab(veces):
    for i in range(veces):
        pg.press("tab")

def abrir_consola_en_elementos():
    pg.hotkey("ctrl","]")

def retornar_y_pegar():
    pg.hotkey("alt","tab")
    time.sleep(1)
    mover_horizontal()
    time.sleep(1)
    pegar_valor()

def buscador_html(arreglo):
        pg.hotkey("alt","tab")
        time.sleep(1)
        pg.write(arreglo[0])
        pg.hotkey("shift","enter")
        pg.write(arreglo[1])
        pg.hotkey("shift","enter")
        pg.write(arreglo[2])
        pg.press("enter")
        time.sleep(1)
    

def recargar_pagina():
    pg.hotkey("shift","ctrl","j")
    pg.press("f5")


contadorVertical = 0
contadorHorizontal = 0

#cambiar al archivo de excel
time.sleep(0.5)
pg.hotkey("alt","tab")
time.sleep(0.5)



    
if contadorHorizontal == 0:
    time.sleep(1)
    mover_vertical()
    copiar_celda()
    time.sleep(1)
    abrir_chrome()
    time.sleep(1)
    continuar()
    maximizar_ventana()
    presionar_tab(17)
    pegar_valor()
    presionar_tab(3)
    press_enter()

    #presionar lupa
    continuar_presionar_lupa()

    # dibujar html presionando el logo
    continuar_logo_consulta()
    time.sleep(1)
    abrir_consola_en_elementos()
    time.sleep(1)

    
    pg.write('let c = document.getElementById("cphMostrarPaginas_lblColorAnimal")')
    pg.hotkey("shift","enter")
    pg.write('let vC = c.innerText')
    pg.hotkey("shift","enter")
    pg.write('copy(vC)')
    pg.press("enter")

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar la fecha de nacimiento
    buscador_html(nacimientos)

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar el padre
    buscador_html(padres)

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar la madre
    buscador_html(madres)

    #volver al archivo de excel
    retornar_y_pegar()

    # #vuelve a la consola a buscar la propietario
    buscador_html(propietarios)

    #volver al archivo de excel
    retornar_y_pegar()

    #descargarPDF
    pg.hotkey("alt","tab")
    time.sleep(0.5)
    pg.write(descargar_PDF1)
    pg.hotkey("shift","enter")
    pg.write(descargar_PDF2)
    press_enter()

    contadorHorizontal += 1
    

while contadorHorizontal == 1:
    
    #mover a siguiente fila
    pg.hotkey("alt","tab")
    time.sleep(1)
    retornar_columna1()
    mover_vertical()
    copiar_celda()
    time.sleep(1)

    #retornar a la pagina y recargarla
    pg.hotkey("alt","tab")
    time.sleep(1)
    recargar_pagina()
    time.sleep(1)
    continuar()
    time.sleep(1)
    presionar_tab(17)
    time.sleep(1)
    pegar_valor()
    time.sleep(1)
    presionar_tab(3)
    press_enter()

    #presionar lupa
    continuar_presionar_lupa()

    # dibujar html presionando el logo
    continuar_logo_consulta()
    time.sleep(1)
    abrir_consola_en_elementos()
    time.sleep(1)
    pg.write('let c = document.getElementById("cphMostrarPaginas_lblColorAnimal")')
    pg.hotkey("shift","enter")
    pg.write('let vC = c.innerText')
    pg.hotkey("shift","enter")
    pg.write('copy(vC)')
    pg.press("enter")

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar la fecha de nacimiento
    buscador_html(nacimientos)

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar el padre
    buscador_html(padres)

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar la madre
    buscador_html(madres)

    #volver al archivo de excel
    retornar_y_pegar()

    #vuelve a la consola a buscar la propietario
    buscador_html(propietarios)

    #volver al archivo de excel
    retornar_y_pegar()

    #descargarPDF
    pg.hotkey("alt","tab")
    time.sleep(0.5)
    pg.write(descargar_PDF1)
    pg.hotkey("shift","enter")
    pg.write(descargar_PDF2)
    press_enter()

