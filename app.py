import numpy as np
import clr
import sys
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from setup import setup

pid = str(input("Input Planter ID: "))

print ("1 = Aster")
print ("2 = Iris")
print ("3 = Marsh Marigold")


type = int(input("Choose Plant Type: "))
print("You chose ")
if (type == 1):
     print("Aster")
     num = 700
if (type == 2):
    print("Iris")
    num = 500
if (type == 3):
    print("Marsh Marigold")
    num = 300

#Threshold just for demo
print("num = ")
print(num)

setup("default", 1024, 0)
#if(level < 1):
    #print("Tank Refill Needed")
