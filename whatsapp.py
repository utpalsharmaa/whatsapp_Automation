import pyautogui as pg
import time
import random

#for know msg location
#time.sleep(5)
#print(pg.position())

n=int(input("Enter no of times:"))
msg_list=['type your msg here']
pg.click(x=1556,y=963) 
for i in range(n):
    pg.write(random.choice(msg_list))
    pg.press("enter")
    print(i)