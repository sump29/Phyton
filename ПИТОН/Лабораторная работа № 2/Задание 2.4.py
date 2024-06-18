import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = math.cos(math.sqrt(x**2 - x) / math.sqrt(a**2 + b**2))


print("a =", a)
print("b =", b)
print("x =", x)
print("y =", y)


print("Целая часть y =", math.floor(y))