# Functions are used to make code more readable and reusable
pos = 5

# def move():
#  global pos
#  pos += 1

#def move(byAmount):
#  global pos
#  pos += byAmount
#move(5)
#print(pos)

def move(pos, byAmount):
  newPos = pos + byAmount
  return newPos

finalPos = move(1, 5)
print(finalPos)  

# skibbady bop boom pow

def happy_birthday(name, age):
  print("Happy birthday to you")
  print("Happy birthday to you")
  print(f"Happy birthday dear {name}")
  print(f"You are {age} years old")
  print()

happy_birthday("max", "20")
happy_birthday("jake", "12")

# skibbady bop boom pow

def display_invoice(username, amount, due_date):
  print(f"Hello {username}")
  print(f"Your bill of ${amount} is due: {due_date}")
  print()

display_invoice("Max", 42.50, "01/01")
display_invoice("Jake", 9.99, "01/02")

#functions are so amazing 

def name(first, last):
  print(f"Hello {first} {last}")

name("Max", "Estrella")
name("Jake", "Ashdown")