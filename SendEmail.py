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