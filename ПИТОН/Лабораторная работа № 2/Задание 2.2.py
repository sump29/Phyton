import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
t = float(input("Введите значение t: "))


x = b * math.sin(a * t**2) * math.cos(2 * t - 1)


print(f"Значение a: {a}")
print(f"Значение b: {b}")
print(f"Значение t: {t}")
print(f"Значение x: {x}")


print(f"Целая часть x: {math.floor(x)}")