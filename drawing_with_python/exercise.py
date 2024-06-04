#pip install pyautogui
# https://jspaint.app/
import pyautogui
from time import sleep
from mss import mss, tools

path = 'Automation/drawing_with_python/'
sleep(1)
position = pyautogui.position()
t = 2
#CORES
marrom = (1264, 958)
amarelo_claro = (1167, 976)
roxo = (1239, 956)
preto = (1009, 959)
cinzacl = (1032, 975)
azul = (1126, 978)
marromcl = (1167, 958)


def pencil():
    lapis = (985, 271)
    last_position = pyautogui.position()
    pyautogui.moveTo(lapis, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(last_position, duration=0.5)
   
def elipse():
    circulo = (980, 393)
    last_position = pyautogui.position()
    pyautogui.moveTo(circulo, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(last_position, duration=0.5)

def straight_line():
    reta = (978, 335)
    linha_grossa = (989, 466)
    last_position = pyautogui.position()
    pyautogui.moveTo(reta, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(linha_grossa, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(last_position, duration=0.5)
   
def paint(cor, x, y):
    balde = (1008, 213)
    last_position = pyautogui.position()
    pyautogui.moveTo(balde, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(cor, duration=0.5)
    pyautogui.click()
    if x > 0 and y > 0:
        last_position = (x-10, x-10)
    if x >0 and y < 0:
        last_position= (x-10, y+10)
    if x < 0 and y > 0:
        last_position =(x+10, y-10)
    else:
        last_position=(x+10, y+10)
    pyautogui.moveTo(last_position, duration=1)
    pyautogui.click()
    pyautogui.moveTo(x=1013, y=956)
    pyautogui.click()
 
    
def square():
    quadrado = (981, 362)
    reta = (978, 335)
    linha_fina = (989, 420)
    last_position = pyautogui.position()
    pyautogui.moveTo(reta, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(linha_fina, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(quadrado, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(last_position, duration=0.5)
 

# SHAPE
straight_line()
pyautogui.moveTo(x=1084, y=790)
pyautogui.drag(200, 0, duration = t, button='left')
pencil()
pyautogui.drag(100, 0, duration = t, button='left')
straight_line()
pyautogui.drag(0, -150, duration = t, button='left')
pyautogui.drag(320, 0, duration = t, button='left')
pyautogui.drag(0, -350, duration = t, button='left')
pyautogui.drag(-280, 0, duration = t, button='left')
pencil()
pyautogui.drag(-100, 0, duration = t, button='left')
straight_line()
pyautogui.drag(-240, 0, duration = t, button='left')
pyautogui.drag(0, 500, duration = t, button='left')

pyautogui.moveTo(x=1084, y=483)

pyautogui.drag(140, 0, duration = t, button='left')
pencil()
pyautogui.drag(100, 0, duration = t, button='left')
straight_line()
pyautogui.drag(0, -200, duration = t, button='left')

pyautogui.moveTo(x=1084, y=637)

pyautogui.drag(200, 0, duration = t, button='left')
pyautogui.drag(0, 40, duration = t, button='left')
pencil()
pyautogui.drag(0, 50, duration = t, button='left')
straight_line()
pyautogui.drag(0, 65, duration = t, button='left')

pyautogui.moveTo(x=1703, y=546)

pyautogui.drag(-100, 0, duration = t, button='left')

# #SACADA
# square()
# pyautogui.moveTo(x=1083, y=212)   
# pyautogui.drag(400, 82, duration = t, button='left')
# paint(amarelo_claro, x=1083, y=212)

# #QUARTO CAMA
# square()
# pyautogui.moveTo(x=1189, y=289)   
# pyautogui.drag(100, 160, duration = t, button='left')
# pyautogui.moveTo(x=1238, y=289)
# pencil()   
# pyautogui.drag(0, 160, duration = t, button='left')
# pyautogui.moveTo(x=1189, y=330)
# pyautogui.drag(100, 0, duration = t, button='left')
# paint(amarelo_claro, x=1083, y=212)

# #QUARTO CÔMODO
# square()
# pyautogui.moveTo(x=1085, y=370) 
# pyautogui.drag(55, 75, duration = t, button='left')
# paint(marrom, x=1085, y=370)

# #ESCRITÓRIO
# square()
# pyautogui.moveTo(x=1144, y=481) 
# pyautogui.drag(75, 55, duration = t, button='left')
# paint(marrom, x=1144, y=481)

# #BANHEIRO - BANHEIRA
# square()
# pyautogui.moveTo(x=1160, y=637) 
# pyautogui.drag(130, 40, duration = t, button='left')
# elipse()
# pyautogui.moveTo(x=1160, y=637) 
# pyautogui.drag(130, 40, duration = t, button='left')
# paint(azul, x=1160, y=637)


# #BANHEIRO - PIA
# square()
# pyautogui.moveTo(x=1151, y=747) 
# pyautogui.drag(66, 42, duration = t, button='left')
# paint(cinzacl, x=1151, y=747)
# elipse()
# pyautogui.moveTo(x=1166, y=746) 
# pyautogui.drag(38, 38, duration = t, button='left')


# #BANHEIRO - VASO
# square()
# pyautogui.moveTo(x=1095, y=766) 
# pyautogui.drag(42, 22, duration = t, button='left')
# paint(cinzacl, x=1095, y=766)
# elipse()
# pyautogui.moveTo(x=1106, y=737) 
# pyautogui.drag(24, 33, duration = t, button='left')
# paint(cinzacl, x=1106, y=737)


# #COZINHA
# square()
# pyautogui.moveTo(x=1388, y=504) 
# pyautogui.drag(70, 140, duration = t, button='left')
# paint(marrom, x=1388, y=504)
# square()
# pyautogui.moveTo(x=1456, y=580) 
# pyautogui.drag(150, 60, duration = t, button='left')
# square()
# pyautogui.moveTo(x=1500, y=583) 
# pyautogui.drag(66, 42, duration = t, button='left')
# paint(cinzacl, x=1500, y=583)
# elipse()
# pyautogui.moveTo(x=1515, y=583) 
# pyautogui.drag(38, 38, duration = t, button='left')
# square()
# pyautogui.moveTo(x=1659, y=475) 
# pyautogui.drag(45, 75, duration = t, button='left')
# paint(marrom, x=1659, y=475)
# elipse()
# pyautogui.moveTo(x=1535, y=437) 
# pyautogui.drag(70, 70, duration = t, button='left')
# paint(marromcl, x=1535, y=437)

# #SALA - SOFA
# square()
# pyautogui.moveTo(x=1624, y=292) 
# pyautogui.drag(81, 130, duration = t, button='left')
# paint(roxo, x=1624, y=292)
# square()
# pyautogui.moveTo(x=1624, y=306) 
# pyautogui.drag(62, 105, duration = t, button='left')
# pencil()
# pyautogui.moveTo(x=1624, y=336) 
# pyautogui.drag(62, 0, duration = t, button='left')
# pyautogui.moveTo(x=1624, y=372) 
# pyautogui.drag(62, 0, duration = t, button='left')

# #SALA - MESA
# square()
# pyautogui.moveTo(x=1508, y=327) 
# pyautogui.drag(60, 70, duration = t, button='left')
# paint(marromcl, x=1508, y=327)

# #SALA - TV
# square()
# pyautogui.moveTo(x=1323, y=290) 
# pyautogui.drag(30, 200, duration = t, button='left')
# paint(marrom, x=1323, y=290)
# square()
# pyautogui.moveTo(x=1340, y=315) 
# pyautogui.drag(10, 110, duration = t, button='left')
# paint(preto, x=1340, y=315)

with mss() as screen:
    part = {'top':200, 'left':1050, 'width':690, 'height':600}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output=path+'output2.png')