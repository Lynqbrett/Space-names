import requests
import json
import pandas as pd

# apt-get install python python-dev python-pip virtualenvwrapper redis-server

space = requests.get('http://api.open-notify.org/astros.json')

space_dict = space.json()
print(["message"])

good = json.dumps(space_dict, indent= 4)
print(good)

x = space_dict["people"]


print("number of people in space: ", space_dict["number"])
print("\npeople currently in space:")
print("craft                         name")
x = 0
while x < 15:
    print(space_dict["people"])
    x+1














































































