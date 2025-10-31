roll_no = {
    "Reema": 1,
    "Seema":2,
    "Jullie": 3,
    "Haka": 4,
    "Haka":5
}

roll_no_2 = dict({   
    "Reema": 1,
    "Seema":2,
    "Jullie": 3,
    "Haka": 4,
    "Haka":5})

roll_no_3 = dict([("Reema", 1234), ("Seema", 3456), ("Jullie", 7890)])
print(roll_no)

print(roll_no_2)

print(roll_no_3)

# adding new item to dictionary
roll_no_3["Haka"] = {1111,2222,3333}
print(roll_no_3)

roll_no_3["Jullie"] = {'Jullie Company A':9876, 'Jullie Company B':345}

# roll_no_3["Jullie"] = {
#     "Jullie Company A": 9876,
#     "Jullie Company B": 345
# }

print(roll_no_3)

print(roll_no_3['Jullie'])
print(roll_no_3["Jullie"]['Jullie Company A'])

print(roll_no_3.get('Haka'))

data = {
    1 : "ronnie",
    2: "ronney",
    0: "randy"
}

print(data[0])

#for deletion of key from dictionary


del roll_no_3['Reema']
print(roll_no_3)

print(roll_no_3.keys())
print(roll_no_3.values())
print(roll_no_3.items())