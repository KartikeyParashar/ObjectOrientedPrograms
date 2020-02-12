import json

class Inventory:
    def __init__(self,dictionary):
        self.seed_brand = dictionary.get("Name")
        self.seed_brand_price = dictionary.get("Price per kg")
        self.seed_brand_weight = dictionary.get("Weight")

class InventoryManager:
    def __init__(self):
        self.lst = []
    
    def calculate_price(self):
        sum = 0
        for obj in self.lst:
            sum += obj.seed_brand_price*obj.seed_brand_weight
        return sum


obj_of_inventory_manager = InventoryManager()


file = open("inventory.json", 'r')
data = json.load(file)
file.close()

for key, value in data.items():
    for dictionary in value:
        obj = Inventory(dictionary)
        obj_of_inventory_manager.lst.append(obj)
        

print(f"The total inventory price of our stock we have is : Rs. {obj_of_inventory_manager.calculate_price()}/-")
