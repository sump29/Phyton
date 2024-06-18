import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = (a ** (2 * x) + b * math.cos(a + b * x)) / (x + 1)


print(f"Значение a: {a}")
print(f"Значение b: {b}")
print(f"Значение x: {x}")
print(f"Значение y: {y}")


print(f"Целая часть y: {int(y)}")