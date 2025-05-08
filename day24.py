# file = open("my_text.txt")  # build in methode, braucht natürlich resourcen
# contents = file.read()
# print(contents)
# file.close()  # freeing the resources, but a better method is:

# with open("my_text.txt") as file:  # damit spart man sich das schließen
#     # contents = file.read()
#     # print(contents)
#     file.write("I love my fishy")  # das funktioniert nicht, weil das hier nur ein read only file ist
#
# with open("my_text.txt", mode="w") as file: # mode="w" write only (default ist "r" read only)
#     contents = file.read() # jetzt steht e auf write only
#     print(contents)
#     file.write("I love my fishy")

# with open("my_text.txt", mode="w") as file:
#     file.write("I love my fishy")  # der komplette vorherige text ist nun weg und ein neuer steht dort

# with open("my_text.txt", mode="a") as file:  # "a" für append
#     file.write("\nI love my fishy")

# with open("created_file.txt", mode="w") as file:
#     file.write("The file didn't exist before. Just by the method open()")

# bisher waren die Dateipade als relative Dateipfade immer im gleichen Ordner, in dem man sich befand
# ausgeschríeben würde das ./my_text.txt sein, das ./ kann man sich aber sparen
# mit einem alcoluten Pad, sehe das so aus:

# with open("/path/data.txt") as file:
#     #  man kann den Pfad nicht 1:1 kopieren, denn der Pfad wird hier NICHT mit backslash angegeben,
#     # sondern mit FORWARD SLASH
#     print(file.read())

# den gleichen Pfad kann man auch als realtiven Pfad von dieser Datei aus angeben:
# with open("../snake_game/data.txt") as file:  # der erste Punkt ist der aktuelle Ort, der zweite ist ein Ort darüber
#     # in dem Fall also: in Ordner day-24, eine hierarchie höher (".") PycharmProjects
#     # und dann con dort aus in den Ornder snake_game
#     print(file.read())

# möchte man realtiv gesehen mehrere Postionen nach oben:
# ../../ sind zwei Ebenen also: Annika Programmierübungen