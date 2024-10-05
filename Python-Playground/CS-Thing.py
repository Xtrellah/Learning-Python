activeSkinDrops = ["The 2018 Inferno Collection", "The 2018 Nuke Collection", "The Bank Collection", "The Italy Collection", "The Lake Collection", "The Safehouse Collection", "The Train Collection", "The Dust 2 Collection"]
activeCaseDrops = ["Kilowatt Case", "Revolution Case", "Recoil Case", "Dreams & Nightmares Case", "Fracture Case"]

print("For CS bindings, type 1.")
print("For CS general information, type 2.")
input("What would you like to see? ")

if input == ("1") :
  print("CS bindings:")
  print("https://github.com/Kyrii-Gaming/CS-Bindings")
if input == ("2") :
  print("Type 'dp' for active drop pool; 'cs' for case drops; 'sk' for skin drops.")
else:
  print("input not recognized")