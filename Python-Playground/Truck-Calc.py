deck = input("Enter your deck size: ")
deck = float(deck)

if float(deck) >= 7.25 and float(deck) <= 8:
  print("You require size 5 or 129mm trucks.")
elif float(deck) >= 8 and float(deck) <= 8.5:
  print("You require size 5.25 or 133mm trucks.")
elif float(deck) >= 8.5 and float(deck) <= 9:
  print("You require size 5.5 or 139mm trucks.")
elif float(deck) >= 9 and float(deck) <= 9.5:
  print("You require size 5.75 or 146mm trucks.")
elif float(deck) >= 9.5 and float(deck) <= 10:
  print("You require size 6 or 152mm trucks.")
elif float(deck) >= 10 and float(deck) <= 11:
  print("You require size 6.5 or 165mm trucks.")
else:
  print("That is not a valid deck size.")