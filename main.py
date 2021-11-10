import time
import pyautogui as pg
from PIL.ImageOps import grayscale
from numpy import true_divide


# numero = 0;


# # while numero < 5:

# #     pg.moveTo(10,10,2)
# #     pg.rightClick()
# #     pg.moveTo(20,15,0.2)
# #     pg.leftClick()
# #     numero += 1


# # pg.moveTo(10,10,2)
# # pg.rightClick()
# # pg.moveTo(20,15,0.2)
# # pg.leftClick()


# # print("Hola mundo1")
# # time.sleep(2)
# # print("Hola mundo2")
# # time.sleep(2)
# # print("fIN")


# #obtener el ancho de la pantalla

# anchoPantalla, altoPantalla = pg.size()
# print(anchoPantalla)
# print(altoPantalla)


# #obtener la posición del mouse

# mouseX, mouseY = pg.position()
# print("------------")
# print(mouseX)
# print(mouseY)

# #mover mouse

# #pg.moveTo(1900,900,2)
# pg.moveTo(50,10,1)

# #Hacer click
# pg.click()

# #Mover de una vez y hacer click
# pg.click(100,10,1)

# #mover hacia un punto especificado por nombre

# pg.click(130,1055,1)
# # pg.click(r'C:\Users\Jhon Romero\Downloads\firma.jpg')

# ##hacer doble click
# # pg.moveTo(1400,800)
# # pg.doubleClick()

# ##escribir
# pg.moveTo(700,600)
# pg.click()
# #pg.write("Esto es un boEsto es un bot!t!")


# # contado = 0
# # y = 600

# # while contado <5:
# #     pg.moveTo(700,y,0)
# #     pg.click()
# #     pg.write("#Esto es un boEsto es un bott!")
# #     pg.press("enter")
# #     contado += 1


# #mover scroll
# pg.moveTo(700,600,1)
# # -hacia abajo, sin singno hacia arriba
# pg.scroll(-200)
# pg.click()

# ##sostener de tecla, subir dos veces


# with pg.hold("alt"):
#     pg.press(["up","up"])


# ##combinar teclas
# pg.hotkey("alt","64")


# #Alertas
# pg.alert("oeoeoe")

# ##Usar el drag en el mouse
# pg.drag(100,15,duration=3)


##validar una posición dentro de la pantalla
print(pg.onScreen(1222,1222))
print(pg.onScreen(122,12))


##cambiar el valor de pause por defecto
#pg.PAUSE = 0.5

#quitar la excepción cuando llega a las esquinas de la pantalla
#pg.FAILSAFE = True

# USAR OFFSET

anchoPantalla, altoPantalla = pg.size()
# pg.moveTo(anchoPantalla/2,altoPantalla/2)
# pg.moveRel(400,0,duration=2)

# ##usar drag relativo
# pg.moveTo(anchoPantalla/2,altoPantalla/2)
# pg.dragRel(-200,-50,duration=2)

## presionar varias veces un botón del ratón

# pg.click(anchoPantalla/2,altoPantalla/2,10,1,"right")


##Mouse Down y mouse up
#pg.moveTo(anchoPantalla/2,15)
# pg.mouseDown(anchoPantalla/2,15)
# pg.moveTo(anchoPantalla/2 + 400,45)


#escribir con caracteres especialñes

# pg.click(anchoPantalla/2,altoPantalla/2)
# pg.typewrite("Hola care nalga Occaecat Lorem laborum amet cillum nisi labore ad qui aliqua cillum consequat. Officia nulla commodo eiusmod mollit ad reprehenderit elit proident. Laboris id eu aliqua eu amet. Quis exercitation ea nisi mollit commodo magna ullamco culpa fugiat. Officia officia enim enim elit dolor adipisicing culpa incididunt incididunt voluptate qui sint amet velit. Aute aliqua eiusmod in magna velit deserunt aliqua et aliquip. \n oelo \ttab",0.01)

#imprimir llaves del teclado
#print(pg.KEYBOARD_KEYS)

#combinar teclas
# pg.moveTo(anchoPantalla/2,altoPantalla/2,2)
# pg.click()
# pg.write("HOEOEOE")
# pg.hotkey("win","e")



### message box confirm
# pg.moveTo(anchoPantalla/2,altoPantalla/2,1)
# boton =pg.confirm("Desea continuar","seleccione",["si","no","quieres un dinero chingón","ACM1PT"])
# print(boton)


# ##prompt
# pg.moveTo(anchoPantalla/2,altoPantalla/2,1)
# mensaje = pg.prompt("oeoeoe")
# print(mensaje)


###scroll horizontal
# pg.moveTo(anchoPantalla/2,altoPantalla/2,1)
# pg.click()
# pg.hscroll(600)



#### programa de terror

# pg.hotkey("win","s")
# pg.write("paint")
# pg.press("enter")
# pg.moveTo(354,60,1)
# pg.click()
# pg.moveTo(anchoPantalla/4,altoPantalla/2)
# pg.click()
# pg.typewrite("Se lo que hiciste el verano pasado \n TE ESTOY OBSERVANDO JULIAAAAAAAAAAN!!!",0.2)

pg.moveTo(anchoPantalla/4,altoPantalla/2)

r = pg.locateCenterOnScreen(r"C:\Users\Jhon Romero\Downloads\nav-btn.PNG")
print(r)
pg.click(r)
