import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = math.sqrt((b * x) / a) + math.cos(x + b)**3


print(f"Значение a: {a}")
print(f"Значение b: {b}")
print(f"Значение x: {x}")
print(f"Значение y: {y}")


print(f"Целая часть y: {math.floor(y)}")