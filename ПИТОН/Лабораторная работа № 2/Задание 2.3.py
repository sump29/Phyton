a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
x = float(input("Введите значение x: "))


y = x**2 + b - b**2 * (x + a)**3 * (x / a)


print("Значение a =", a)
print("Значение b =", b)
print("Значение x =", x)
print("Значение y =", y)


print("Целая часть значения y =", int(y))