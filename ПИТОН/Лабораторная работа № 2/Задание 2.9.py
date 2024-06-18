import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = math.sqrt(x**2 + b - b**2 * math.sin((3 + a) * x))


print("Значение a =", a)
print("Значение b =", b)
print("Значение x =", x)
print("Значение y =", y)


print("Целая часть y =", math.floor(y))