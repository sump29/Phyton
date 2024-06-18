import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = x**2 * (x + 1) / b - math.sin(x + a)


print(f"Значение a: {a}")
print(f"Значение b: {b}")
print(f"Значение x: {x}")
print(f"Значение y: {y}")


print(f"Целая часть y: {int(y)}")