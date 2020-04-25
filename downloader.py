from selenium import webdriver
import time
from pynput import mouse, keyboard
TITLE="""

DDDDD            OOOOOO             LLL
D    DD            OOOOOO           LLL
D     DD            OOOOOO          LLL
D      DD            OOOOOO         LLL
D       DD            OOOOOO        LLL
D        DD            OOOOOO       LLL
D       DD            OOOOOO        LLL
D      DD            OOOOOO         LLL
D     DD            OOOOOO          LLL
DDDDDD             OOOOOO           LLLLLLLLLLLLLL


BY darscade.ir


"""
khat=r"""
*************************************************************************
+++++++++++++++++++++||| D A R S C A D E . I R |||+++++++++++++++++++++++
*************************************************************************
"""

print(TITLE)
print(khat+"\n\n")

f = open(input('Enter url.txt : '),"r")
y = f.readlines()
f.close()
print(y)
kb = keyboard.Controller()
for i in range(0, len(y)):
    time.sleep(1)
    line = y[i].strip()
    z=line.split("\n")
    print(z[0])
    Chrome = webdriver.Firefox()
    #time.sleep(7)
    Chrome.get(z[0])
    mos = mouse.Controller()
    mos.position = (400, 400)
    mos.click(mouse.Button.left, 1)
    mos.click(mouse.Button.right, 1)
    mos.move(30, 200)
    mos.move(30, 0)
    time.sleep(1)
    mos.click(mouse.Button.left, 1)
    time.sleep(10)
    # break
    kb.press(keyboard.Key.enter)
    time.sleep(3)
    Chrome.quit()
    print('loocked to site : '+z[0])
print('sites in the file, is end')
print('program ended.')