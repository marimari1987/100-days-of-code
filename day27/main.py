from tkinter import *  # alles importieren, aber die klasse muss nicht mehr angesprochen werden

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)   # macht einen leeren "rahmen" um die eingabefläche

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack() # bevor man diese Zeile schreibt, wird nichts angezeigt
# pack gibt keine Paramter an, aber **kw sind optonal keyword argments siehe playground
# https://docs.python.org/3/library/tkinter.html#the-packer
# in funktionen: wenn in der beschreibung z.B. font: str=... steht, hat es schon default werte

my_label.grid(column=0, row=0)  # wenn man grid nutzt, muss das erste bei colun=0 row=0 liegen
my_label["text"] = "New Text"  # eine ander Möglichkeit den text zu ändern
my_label.config(text="The Latest Text")  # oder auch so
# my_label.config(padx=50, pady=50) # man kann auch einen rahmen um die einzelnen komponenten machen

# Button


def button_clicked():
    # print("I got clicked")  # wird in der Konsole ausgegeben
    # my_label.config(text="I got clicked")  # ändert den Text des Labels
    my_label.config(text=text_field.get())  # schreibt den Text aus dem text_field


button = Button(text="Click me", command=button_clicked)  # aufpassen, dass bei der funktion KEINE Klammern sind
# button.pack()
button.grid(column=1, row=1)

# Entry

text_field = Entry(width=20)
# text_field.pack()
text_field.grid(column=3, row=2)

# weitere Widgets als Beispiele
# tkinter_widgets_demo hier im PYcharm
# https://replit.com/@appbrewery/tkinter-widget-demo

# button2 = Button(text="Button 2")
# button2.place(x=100, y=200)  # im unterschied zu pack, kann man eine position wählen

button3 = Button(text="Button 3")
button3.grid(column=2, row=0)  # grid() funktioniert nicht zusammen mit pack()

window.mainloop()
