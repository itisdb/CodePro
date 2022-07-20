import pyautogui as pg
import time 

time.sleep(10)

txt = open('animals.txt','r')

for i in txt:
	pg.write(i)
	pg.press('Enter')