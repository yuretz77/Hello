people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name": "Cho","house":"Ravenclaw"},
    {"name": "Draco", "house":"Skytherin"}
]

#def f(person):
#    return person["name"]

#people.sort(key=f)

people.sort(key = lambda person: person["name"])
print(people)