from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # https://colorhunt.co/palettes
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1  # 25
SHORT_BREAK_MIN = 0.2  # 5
LONG_BREAK_MIN = 20  # 20
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer_count
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        reps = 0
    if reps % 2 == 0:  # 0,2,4,6 Work
        time = work_sec
        title_label.config(text="Work", fg=GREEN)
    elif reps <= 5:  # 1,3,5
        window.attributes('-topmost', 1)  # bringt das Fenster in den Vordergrund, funktoniert aber nicht minimiert
        window.attributes("-topmost", 0)  # sollte topmost canceln, tut es nicht, außer man minimiert es
        time = short_break_sec
        title_label.config(text="Short Break", fg=PINK)
    else:  # 7
        time = long_break_sec
        title_label.config(text="Long Break", fg=RED)
    count_down(time)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# den countdown mechanism kann man nicht mit time machen, weil die while schleife verhindern würde,
# dass die mainloop schleife ausgeführt wird. Es wrde also ncht mal das fenser zu stande kommen


def count_down(count):
    minutes = int(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{count % 60}"  # Dynamic Typing, erst war es ein int etzt ist es ein str
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)  # nach 1000ms funktion mit dem argument
    else:
        start_timer()
        marks = ""
        working_time = int(reps/2)
        for _ in range(working_time):
            marks += "✓"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# Window


window = Tk()
window.title("Pomodoro Working Timer")
window.config(padx=100, pady=50, bg=YELLOW)  # bg=background

# Hintergund als Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # um overlaps zu machen ein bild auf einem bild
# highlightthickness macht den rand weg, der sonst noch weiß wäre
image = PhotoImage(file="tomato.png")  # kovertierung um es zu nutzen
canvas.create_image(100, 112, image=image)  # musste erst kovertiert werden, die zahlen sind x und y
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Arial", 25))  # fg=frontground color
title_label.grid(column=1, row=0)
checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

# buttons
start = Button(text="start", width=8, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="reset", width=8, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
