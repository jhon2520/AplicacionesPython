import time
from PIL.ImageOps import grayscale
import pyautogui as pg 

pg.alert("Código iniciado")
pg.hotkey("win","e")
time.sleep(1)
escritorio = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\bot-imgs\escritorio.PNG", grayscale = True,confidence=0.8)
pg.click(escritorio)
time.sleep(0.5)
correo = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\bot-imgs\correo.PNG", grayscale = True,confidence=0.8)
pg.doubleClick(correo)
time.sleep(0.5)
texto = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\bot-imgs\texto.PNG", grayscale = True,confidence=0.8)
pg.doubleClick(texto)
time.sleep(1)
pg.keyDown("shiftleft")
pg.keyDown("shiftright")
pg.keyDown("ctrl")

contador = 0

while contador < 8:
    pg.hotkey("right","right","right")
    contador+=1;

pg.keyUp("shiftleft")
pg.keyUp("shiftright")
pg.keyUp("ctrl")

pg.hotkey("ctrl","c")
pg.hotkey("alt","space")
pg.press(["up","enter"])
time.sleep(1)
pg.hotkey("win","win","t")
pg.press(["up","enter"])
time.sleep(1)
pg.hotkey("ctrl","t")
pg.write("mai")
pg.press("enter")


#Abrir Email
continuar = False

while not continuar:
    email = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Desktop\bot-imgs\email.PNG",grayscale=True,confidence=0.8)
    if email != None:
        continuar = True
        pg.click(email)

time.sleep(3)
pg.typewrite("cindya",0.05)
pg.press(["tab","enter","tab"])
pg.write("Correo automático cindy chupona")
pg.press("tab")
pg.hotkey("ctrl","v")
pg.press(["tab","enter"])




# print(pg.KEY_NAMES)

#C:\Users\Jhon Romero\Desktop\bot-imgs

# buscar_color1 = 'let color = document.getElementById("cphMostrarPaginas_lblColorAnimal")'
# buscar_color2 = 'let valorColor = color.innerText'
# buscar_color3 = "copy(valorColor)"


# buscar_nacimiento1 = 'let fecha = document.getElementById("cphMostrarPaginas_lblFecNacimiento")'
# buscar_nacimiento2 = 'let valorFecha = fecha.innerText'
# buscar_nacimiento3 = 'copy(valorFecha)'

# buscar_padre1 = "let padre = document.getElementById('cphMostrarPaginas_lblNumeroPadre')"
# buscar_padre2 = "let valorPadre = padre.innerText"
# buscar_padre3 = "copy(valorPadre)"

# buscar_madre1 = "let madre = document.getElementById('cphMostrarPaginas_lblNumeroMadre')"
# buscar_madre2 = "let valorMadre = madre.innerText"
# buscar_madre3 = "copy(valorMadre)"


# buscar_propietario1 = "let pr = document.getElementById('cphMostrarPaginas_lblNombrePropietario')"
# buscar_propietario2 = "let nPr = pr.innerText"
# buscar_propietario3 = "copy(nPr)"


     # pg.hotkey("alt","tab")
        # time.sleep(1)
        # pg.write(buscar_nacimiento1)
        # press_enter()
        # time.sleep(1)
        # pg.write(buscar_nacimiento2)
        # press_enter()
        # time.sleep(1)
        # pg.write(buscar_nacimiento3)
        # press_enter()
        # time.sleep(1)
        

               # pg.hotkey("alt","tab")
        # time.sleep(1)
        # pg.write(buscar_padre1)
        # press_enter()
        # time.sleep(1)
        # pg.write(buscar_padre2)
        # press_enter()
        # time.sleep(1)
        # pg.write(buscar_padre3)
        # press_enter()
        # time.sleep(1)

               # pg.hotkey("alt","tab")
        # time.sleep(1)
        # pg.write(buscar_madre1)
        # press_enter()
        # time.sleep(1)
        # pg.write(buscar_madre2)
        # press_enter()
        # time.sleep(1)
        # pg.write(buscar_madre3)
        # press_enter()
        # time.sleep(1)

            # pg.hotkey("alt","tab")
    # time.sleep(1)
    # pg.write(buscar_propietario1)
    # press_enter()
    # time.sleep(1)
    # pg.write(buscar_propietario2)
    # press_enter()
    # time.sleep(1.5)
    # pg.write(buscar_propietario3)
    # press_enter()
    # time.sleep(1.5)