import json

file = open("inventory.json", 'r')
data = json.load(file)
file.close()

# for key in data:
#     for value in data[key]:
#         price = 0
#         weight = 0
#         price += value["Price per kg"]
#         weight += value["Weight"]
#         print(f"Name : {value['Name']}")
#         print(f"Price : {value['Price per kg']}")
#         print(f"Weight: {value['Weight']}")

for key, value in data.items():
    print(f"The {key} details are as follows: ")
    for dictionary in value:
        for keys, values in dictionary.items():
            print(f"{keys} : {values}")
    print()


