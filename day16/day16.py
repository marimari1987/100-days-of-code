# import another_module # Beispiel Modul
# print(another_module.variable) # Modul anwählen. was daraus
# from another_module import variable
# print(variable) # so braucht man nicht mehr den Punkt, sondern kann gleich die variable ansteuern
#
# from turtle import Turtle, Screen # das gleiche wie mit dem Beispiel Modul
# # um die Funktionen von turtle anzuschauen: docs.python.org ort in der library turtle
#
# timmy = Turtle()
# print(timmy)  # Das Object timmy der Klasse turtle wird augegeben
# timmy.shape("turtle")
# timmy.color("magenta4") # https://cs111.wellesley.edu/labs/lab01/colors
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth) # my_screen ist das Objekt und canvwidth ist das Attribut
# my_screen.exitonclick()  #ein weiters attribut, a method

#package installieren: file, settings, das projekt, instructor, + , dann das package suchen

#import prettytable # um den code zu sehen, rechtsklick, GotTO, implementation
from prettytable import PrettyTable
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align="l")
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align = "r"
print(table)
print(table.align)