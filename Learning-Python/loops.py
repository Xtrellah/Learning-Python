# LOOPS
# While loops provide a way to execute code multiple times until they return false
pos = 1
endPos = 5

while pos < endPos:
  pos += 1
  print("position is " + str(pos))

# For loops provide a way to execute code a set number of times
inventory = ["sword", "shield", "potion"]

for item in inventory:
  print(item)

for i in range(5):
  print(i)
