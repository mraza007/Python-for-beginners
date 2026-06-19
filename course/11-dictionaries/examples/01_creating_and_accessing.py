"""Creating dictionaries and reading values by key.

Run me:  python 01_creating_and_accessing.py
"""

person = {"name": "Ada", "age": 36}

print(person["name"])    # Ada    look up by key
print(person["age"])     # 36
print(len(person))       # 2      number of key:value pairs

person["age"] = 37            # update an existing key
person["city"] = "London"     # add a brand-new key
print(person)            # {'name': 'Ada', 'age': 37, 'city': 'London'}

# .get() looks up safely — no crash if the key is missing.
print(person.get("email"))          # None
print(person.get("email", "n/a"))   # n/a  (a default you choose)
