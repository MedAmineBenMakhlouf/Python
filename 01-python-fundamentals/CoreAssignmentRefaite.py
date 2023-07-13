x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

# x[1][0]=15
# print(x)

# students[0]['last_name']="Brayant"
# print (students[0])

# sports_directory['soccer'][0]="Andres"
# print(sports_directory['soccer'])

# z[0]['y']=30
# print (z)


# def Affiche(some_list):
#     for student in some_list:
#         print(
#             f"FIRST NAME - {student['first_name']}, LAST NAME - {student['last_name']}"
#         )

# Affiche(students)

# def  iterateDictionary2(key_name, some_list):
#     for sublist in some_list:
#         print(sublist[key_name])

# iterateDictionary2('first_name',students)

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael","Amy","Eduardo","Josh","Graham","Patrick","Minh","Devon",
    ],
}


def printInfo(some_dict):
    for ke,valu in some_dict.items():
        print(f"{len(valu)} - {ke}")
        for item in valu:
            print(item)


printInfo(dojo)
