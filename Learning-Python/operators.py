# Assignment (=))
age = 19
firstname = "Max"
money = 0
savings = 2000

# Arithmatic (+, -, *, /, //, %, **)
newAge = age + 1
fullName = firstname + " Estrella"

# Comparison (==, !=, >, <, >=, <=)
isMaxBroke = money <= 0

# Logical (and, or, not)
isMaxBroke = money <= 0 and savings <= 0
maxIsBalling = not isMaxBroke

print(newAge)
print(fullName)
print(isMaxBroke)

# More examples
temp = 20
sunny = True

if temp <= 0 or temp >= 30:
  print("The temperature is bad")
else:
  print("The temperature is good")

if sunny == True:
  print("It is sunny")
else:
  print("It is cloudy")

if temp >= 0 or temp <= 30 and sunny:
  print("The weather is perfect")
