# Exercise 1
""" The following are all exercises on dictionaries, I have tried to make them as interactive as I could:)
Hope you enjoy.
"""
# A
name = input("Enter ur name: ")
age = int(input("How old r u? "))
city = input("Where do u live: ")
Dict_1 = {
    "Name": name,
    "Age": age,
    "City": city,
}

print()
print(Dict_1.get("Name"))
print(Dict_1.get("Age"))
print(Dict_1.get("City"))
print(Dict_1.get("Hair color", "You haven't entered hair color"))

# B
print()
N = int(input("Number of people:"))
dict = {}
for i in range(N):
    name = input("What is ur name?")
    num = float(input(
        " \t Ur favourite number?"))  # eziga \n bye mehal lay and lela line hula eyetewe nebr why gn bc \n gives new line adel so it will leave a bado mesmer
    dict[name] = num
print()
print(dict)
print()
for key, value in dict.items():
    print(key, ":", value)

# C No way of shortening this is there?
print()
Glossary = {
    "Script": " A shorter line of code used for automating a specific task or sometimes a more complicated one, it has\
    less structured development environment.",
    "\n\t Automation": "is making manually repeated task automatic,but not all tasks are automable.",
    "\n\tClient based programming": "A programming language used to transfer the server info to user's computer and receive\
their information like Javascript for e.g.",
    "\n\tCross-platform": "Compatible with every operating systems.",
    "\n\tOOP object oriented programming": "A programming where elements of a code are going to mimic real life objects\
and are going to have attribute and method.",
    "\n\tComputer programs": "Single executible files that contain all the recipe for how to perform a certain task.",
}
for key in Glossary.keys():
    print(key, "means", Glossary[key])

# we are done with the first exercise.


# Exercise 2

count_riv = {
    "Egypt": "Nile",
    "U.S.A.": "Missiissiippi",
    "XYZ": "Idc",
}
for count in count_riv.keys():
    x = count_riv[count]
    print(f"{x.title()} flows in {count}.")
    print()
    print(x.title())
    print(count.title())
    print()

fav_lan = {
    "Elsi": "python",
    "Ela": "C",
    "Nani": "Ruby",
    "Aba": "Javascript",
}

Should_take_poll = ["Elsi", "Kate", "Ela", "Abebebe", "Kebe", "Paul", "Nani", "Aba"]
for x in Should_take_poll:
    if x in fav_lan.keys():
        print(f"{x.title()}, thank you for taking the poll.")
    else:
        print(f"{x.title()}, please take the poll.")
    print()

# Exercise 3

# A
N = int(input("How many ppl r there?"))
ppl = []
for i in range(N):
    name = input("Name: ")
    Age = int(input("Age:  "))
    city = input("City where u live:  ")
    print()
    dict_i = {
        "name": name,
        "Age": Age,
        "city": city,
    }
    ppl.append(dict_i)

print(ppl)
for i in range(len(ppl)):
    print(ppl[i]['name'])
    print(ppl[i]['Age'])
    print(ppl[i]['city'])
    print()

# B
# we will reuse N
pets = []
for i in range(N):
    M = input("Pet's name:  ")
    name = input("Owner's name:  ")
    Animal_type = input("Pet type:  ")
    print()
    lists= [M, Animal_type]
    dict_1 = {
        "Owners name": name,
        "Pet": lists,
    }
    pets.append(dict_1)

for x in range(N):
    y = pets[x]
    print(f"{y["Owners name"].title()} has a {y["Pet"][1].lower()}. Its name is {y["Pet"][0].title()}.")

    # C
    N = int(input("Number of people:  "))
    dict_12 = {}
    for i in range(N):
        name = input("What is your name?  ")
    print("List three of your favorite places below:")
    A1 = input("1:  ")
    A2 = input("2:  ")
    A3 = input("3:  ")
    fav_pl = [A1, A2, A3]
    dict_12[name] = fav_pl
    for x in dict_12.keys():
        print(f"{x.title()}'s favourite places are:")
    for y in dict_12[x]:
        print(y.title())
    print()

    # D
    N = int(input("Number of ppl:  "))
    dict___1 = {}
    for i in range(N):
        n = input('Your name: ')
    print("List 3 of ut favourite numbers below:")
    A1 = float(input("1:  "))
    A2 = float(input("2:  "))
    A3 = float(input("3:  "))
    fav_nums = [A1, A2, A3]
    dict___1[n] = fav_nums
    print()
    for A in dict___1:
        print(f"{A.title()}'s favorite numbers are:")
    for y in dict___1[A]:
        print(y)
    print()

    print(dict___1)

    # E
    N = int(input("How many ppl are there?  "))
    print("Each of u are going to state three facts about ur cities.")
    print()
    XYZ = {}
    for i in range(N):
        city = input("City name:  ")
    dict = {}
    popn_ = float(input("How many ppl live there?  "))
    country = input("Where is it found?")
    fact = input("State some fact u know about it:  ")
    print()
    dict["population"] = popn_
    dict["fact"] = fact.title()
    dict["contry"] = country.title()
    XYZ[city] = dict

    for X in XYZ:
        print(f"{X.title()} is a city.")
    for y in XYZ[X]:
        print(f"{y.title()} : {XYZ[X][y]}")
    print()

    # Can I Just say WELLDONE to myself:)

    # F
    Alien_0 = {
        'color': 'blue',
        'pts': 25,
        'age': 23,
    }
    Alien_0['sex'] = 'male'
    Alien_0['height(m)'] = 1.25
    Alien_0['killed by'] = 'gun'

    print("Information on Alien_0:")
    for key, value in Alien_0.items():
        if(type(value) != int) and (type(value) != float):
            print(f"\t {key.title()}= {value.title()}")
        else:
            print(f"\t {key.title()}= {value}")






