# Lists starts from 0
inventory = ["sword", "shield", "potion"]

shield = inventory[1]
inventory[1] = "apple"
print(inventory)

# Set to print x ammount
firstTwo = inventory[0:2]
print("First two items: " + str(firstTwo))

# Also abunch of operations avilable 
inventory.append("water")
inventory.insert(1, "Knife")
inventory.remove("sword")
print(inventory)