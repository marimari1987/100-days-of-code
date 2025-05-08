# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_frame = pandas.DataFrame(data)  # man muss es doch nicht dataframen

# for (index, row) in data_frame.iterrows():  # Beispiel wie man die einzelen werte aus dem DataFrame abruft
#    print(row.code)

nato_alphabet = {row.letter : row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Which word du you want to spell in nato phonetic? ").upper()  # soll in Großbuchstaben sein
    # word_letters = list(word)  # braucht man auch nicht

    # result = [value for (key, value) in nato_alphabet.items() if key in word]
    # for letter in word_letters:  # Beispiel ohne Listcomprehension
    #     print(nato_alphabet["letter"])

    try:
        result_2 = [nato_alphabet[letter] for letter in word]  # hier ist es in der richtigen anordnung
    except KeyError:
        print("Sorry, only letters from the american alphabet")
        generate_phonetic()
    else:
        print(result_2)


generate_phonetic()



