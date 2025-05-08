from tkinter import *
from functools import partial

column = 0
row = 1
calc_list = []
result = 0


class CalculatorButton(Button):
    def __init__(self,  **kw):
        super().__init__(font=("Arial", 20, "bold"), **kw)
        global column, row
        self.grid(column=column, row=row, sticky=EW)
        if column < 3:
            column += 1
        else:
            column = 0
            row += 1


def number(num):
    output.insert(END, num)


def reset():
    output.delete(0, END)
    global calc_list, result
    calc_list = []
    result = 0


def clear():
    output.delete(0, END)


def operation(op):  # TODO: Beispiel 12*12= 144 dann - 44 kommt 244 raus
    if output.get() == "":
        new_number = result
    else:
        new_number = float(output.get())
    calc_list.append(new_number)
    calc_list.append(op)
    output.delete(0, END)


def equals():  # TODO: Klammern, das C besser machen, damit man alles oder nur den eingegeben wert löschen kann
    global calc_list, result
    if len(calc_list) == 0:
        result = 0
    else:
        if output.get() == "":
            new_number = 0
        else:
            new_number = float(output.get())
        calc_list.append(new_number)
        output.delete(0, END)
        result += calc_list[0]
        print(calc_list)
        for index in range(1, len(calc_list), 2):
            num_2 = calc_list[index+1]
            operation = calc_list[index]
            if operation == "+":
                result += num_2
            elif operation == "-":
                result -= num_2
            elif operation == "/":
                if num_2 == 0:
                    pass
                else:
                    result /= num_2
            elif operation == "*":
                result *= num_2
    calc_list = []
    output.insert(0, result)
    result = 0


window = Tk()
window.title("Taschenrechner")
window.config(padx=20, pady=20)

output = Entry()
output.grid(column=1, row=0, columnspan=2)

# ---------------- Buttons ---------- #
button1 = CalculatorButton(text=1, command=partial(number, 1))
button2 = CalculatorButton(text=2, command=partial(number, 2))
button3 = CalculatorButton(text=3, command=partial(number, 3))
add_button = CalculatorButton(text="+", command=partial(operation, "+"))
button4 = CalculatorButton(text=4, command=partial(number, 4))
button5 = CalculatorButton(text=5, command=partial(number, 5))
button6 = CalculatorButton(text=6, command=partial(number, 6))
sub_button = CalculatorButton(text="-", command=partial(operation, "-"))
button7 = CalculatorButton(text=7, command=partial(number, 7))
button8 = CalculatorButton(text=8, command=partial(number, 8))
button9 = CalculatorButton(text=9, command=partial(number, 9))
div_button = CalculatorButton(text="/", command=partial(operation, "/"))
equals_button = CalculatorButton(text="=", command=equals)
button0 = CalculatorButton(text=0, command=partial(number, 0))
comma_button = CalculatorButton(text=".", command=partial(number, "."))
multiply_button = CalculatorButton(text="*", command=partial(operation, "*"))

c_button = Button(text="C", command=clear)
c_button.grid(column=3, row=0)

ce_button = Button(text="CE", command=reset)
ce_button.grid(column=0, row=0)

window.mainloop()

