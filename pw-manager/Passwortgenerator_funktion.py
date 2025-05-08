from random import choice, randint, shuffle


def generate_password():
    buchstaben = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    zahlen = list("1234567890")
    zeichen = list('''!"§$%&/()=?*#^°{[]}''')

    # Neue Version mit list comprehension (aus irgendwelchen Gründen muss das in drei Listen):
    passwort_buchstaben_liste = [choice(buchstaben) for _ in range(randint(8, 10))]
    passwort_zeichen_liste = [choice(zeichen) for _ in range(randint(2, 4))]
    passwort_zahlen_liste = [choice(zahlen) for _ in range(randint(2, 4))]

    passwort = passwort_zahlen_liste + passwort_buchstaben_liste + passwort_zeichen_liste

    shuffle(passwort)

    password = "".join(passwort)
    return password