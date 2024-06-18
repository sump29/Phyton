import math


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = math.sin((x**2 + a**2)**(1/3)) - math.sqrt(x/b)


print("Значение a =", a)
print("Значение b =", b)
print("Значение x =", x)
print("Значение y =", y)


print("Целая часть y =", math.floor(y))