import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = math.cos(math.sqrt(x**3 - x)) / math.sqrt(a**2 + b**2)


print("Значение a =", a)
print("Значение b =", b)
print("Значение x =", x)
print("Значение y =", y)


print("Целая часть y =", math.floor(y))