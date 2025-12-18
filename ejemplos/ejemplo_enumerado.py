from enum import Enum
class Color(Enum):
   RED = 1
   GREEN = 2
   BLUE = 3

# x = Color()
x = Color.RED

if x == Color.RED:
    print("es rojo")

if x is Color.RED:
    print("es rojo")

if x.value == 1:
    print("es rojo")

if x.name == Color.RED.name:
    print("es rojo")