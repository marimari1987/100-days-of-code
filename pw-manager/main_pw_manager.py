from tkinter import *
from tkinter import messagebox  # das wird nicht importiert, weil es ein Modul? ist
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Aus dem alten Passwortgenerator
from Passwortgenerator_funktion import generate_password


def retrieve_password():
    password_entry.insert(0, generate_password())
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():  # TODO siehe unten, wenn man save(event) schreibt, geht es mit enter, aber nicht mehr mit klick
    """saves the Website/Email and Password in the data.txt file"""
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    # Zur Vorbereitung für json
    new_data = {website_text.lower(): {
        "email": email_text,
        "password": password_text
        }
    }

    if len(website_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Oops", message="All of the fields need to be filled out")
    else:
        # alter Text ohne json:
        # is_ok = messagebox.askokcancel(title=website_text, message=f"{website_text}\n{email_text}\n{password_text}\n"
                                                                   # f"Is this ok?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data:
                data = json.load(data_file)
                # Updating old data
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):  # fängt auch den Fehler ab, wenn die Datei leer ist
            data = new_data
        finally:
            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)  # macht das Feld wieder leer
            password_entry.delete(0, END)

# ---------------------------Search Password--------------------------- #


def search():
    website_text = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):  # exceptions sollten exceptions bleiben, also sehr selten
        # deshalb kommt da nicht der KeyError rein, den kann man einfach mit if else abdecken.
        new_pw = messagebox.askyesno(title="Create New File?", message="The file doesn't exist yet.\n"
                                           "Do you want to generate a password and save?", default="yes")
        if new_pw:
            retrieve_password()  # TODO: Lösung finden, dass der Button nur noch mit enter bestätigt werden muss
            # add_button.focus_set()
            # window.bind("<Return>", save)
        else:
            website_entry.delete(0, END)
    else:
        if website_text in data:
            password = data[website_text]["password"]
            pyperclip.copy(password)
            email = data[website_text]["email"]
            messagebox.showinfo(title="Your Password", message=f"Your username/email for {website_text} is {email}.\n"
                                                               f"Your password was copied, you can paste it now.")
            website_entry.delete(0, END)
        else:
            new_pw = messagebox.askyesno(title="Create Password?", message="This website doesn't exist yet.\n"
                                                                           "Do you want to generate a password?",
                                         default="yes")
            if new_pw:
                retrieve_password()  # TODO: Lösung finden, dass der Button nur noch mit enter bestätigt werden muss
                # add_button.focus_set()
                # window.bind("<Return>", save)
            else:
                website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

# Grids:
grids = {"website_label": [0, 1], "email_label": [0, 2], "password_label": [0, 3],
         "website_entry": [1, 1], "email_entry": [1, 2], "password_entry": [1, 3],
         "logo": [1, 0],
         "generate_button": [2, 3], "add_button": [1, 4], "search_button": [2, 1]
         }

# Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthicknes=0)
# die größe des Bildes steht in der datei oben rechts in Pycharm
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)  # in der Mitte positionieren
canvas.grid(column=grids["logo"][0], row=grids["logo"][1])

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=grids["website_label"][0], row=grids["website_label"][1])
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=grids["email_label"][0], row=grids["email_label"][1])
password_label = Label(text="Password:", bg="white")
password_label.grid(column=grids["password_label"][0], row=grids["password_label"][1])

# Entrys
website_entry = Entry()
website_entry.grid(column=grids["website_entry"][0], row=grids["website_entry"][1], sticky=EW)
# sticky=EW spannt das Widget über das gesamte grid Feld von (E)ast nach (W)est
website_entry.focus()  # setzt den cursor in das erste eingabefeld
email_entry = Entry()
email_entry.grid(column=grids["email_entry"][0], row=grids["email_entry"][1], columnspan=2, sticky=EW)
email_entry.insert(0, "twixy9@yahoo.de")  # will man das ende, kann man stat 0 END schreiben
password_entry = Entry()
password_entry.grid(column=grids["password_entry"][0], row=grids["password_entry"][1], sticky=EW)

# Buttons
generate_button = Button(text="Generate", command=retrieve_password)
generate_button.grid(column=grids["generate_button"][0], row=grids["generate_button"][1], sticky=EW)
add_button = Button(text="Add", command=save)
add_button.grid(column=grids["add_button"][0], row=grids["add_button"][1], columnspan=2, sticky=EW)
search_button = Button(text="Search", command=search)
search_button.grid(column=grids["search_button"][0], row=grids["search_button"][1], sticky=EW)

window.mainloop()
