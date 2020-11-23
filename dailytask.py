import os
import pyautogui as pe
import time
import subprocess
os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe'),
time.sleep(1),
pe.moveTo(431,116),
pe.click(431,116,1),
time.sleep(0.1),
pe.typewrite('myclass.lpu.in'),
pe.press('enter'),
time.sleep(5),
pe.move(1307,542),
time.sleep(1),
pe.typewrite('1180510'),
time.sleep(1),
pe.move(1280,655,1),
time.sleep(0.5),
pe.typewrite('Anil@2020')