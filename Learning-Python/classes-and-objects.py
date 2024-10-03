# Classes are used to create objects
# Objects are instances of classes
# Objects have attributes and methods
# Attributes are variables that belong to an object
# Methods are functions that belong to an object
#
class GameCharecter:

  def __init__(self, name, pos, health):
    self.name = name
    self.pos = pos
    self.health = health

  def move(self, by_amount):
    self.pos += by_amount

charecter = GameCharecter("MAX", 5, 100)
print(charecter.health)
charecter.health = 120
print(charecter.health)
charecter.move(10)
print(charecter.pos)
print()

newcharecter = GameCharecter("Jim", 0, 100 )
print(newcharecter.name)
print(newcharecter.pos)
print(newcharecter.health)