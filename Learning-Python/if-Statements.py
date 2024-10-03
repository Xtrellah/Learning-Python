# If statements are used to make decisions

pos = 5
key = "d"

if key == "a":
  pos += 1
  print("player moved left")
elif key == "d":
  pos -= 1
  print("player moved right")
else:
  print("Command uknown")

print(pos)