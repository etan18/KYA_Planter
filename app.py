import NumPy
import clr
import System
from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

fburl = string(input("Enter Firebase Database URL"))

 print ("1 = Aster")
 print ("2 = Iris")
 print ("3 = Marsh Marigold")

 plantype = int(input("Choose Plant Type: "))
 print("You chose ")
 if (plantype == 1):
     {
     print("Aster")
     int x = .3
     }
if (plantype == 2):
    {
    print("Iris")
    int x = .5
    }
if (plantype == 3):
    {
    print("Marsh Marigold")
    int x = .7
    }

print("x = ") << print(x)
