#Dictionarys are key vlaue pairs 
inventory = {"sword": 2, "shield": 1, "potion": 3}

numPotions = inventory["potion"]
print("You have " + str(numPotions) + " potions!")
print("You found a potion!")
inventory["potion"] = 4
print("You have " + str(inventory["potion"]) + " potions!")

inventory["cash"] = 500
print("You found some cash!")
print("You have " + str(inventory["cash"]) + " dollars!")

print("Items:")
print(inventory.items())
print("Keys:")
print(inventory.keys())
print("Copy:")
print(inventory.copy())
print("Clear:")
print(inventory.clear())