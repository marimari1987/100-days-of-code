names = ["A", "B", "C", "D"]
grades = [ 67, 24, 75, 25]

student_data = {"student" : [name for name in names], "grade" : [grade for grade in grades]}
# for (key, value) in student_data.items():
#    print(value) # gibt zwei Listen aus, eine mit den keys und eine mit den values

import pandas
student_data_frame = pandas.DataFrame(student_data)
# print(student_data_frame)
# for (key, value) in student_data_frame.items():
#    print(value)  # macht zwei Tabellen mit jeweil der einen Spalte names und der andern spalte grades

for (index, row) in student_data_frame.iterrows():
    #print(row)
    # hier kommen mehrere data.series objects bei heraus.
    # Name: 0, dtype: object
    # students    B
    # grades         24
    #... usw. für jeden Namen ein Ojekt

    print(row.student) # gibt die reihe mit den namen aus
print(student_data_frame.student) # im Unterschied hierzu, das gibt auch die Reihe aus, aber mit dem Index davor