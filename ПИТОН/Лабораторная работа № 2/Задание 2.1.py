x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))


b = abs((x**1/3 - y) / x)


print("Значение x =", x)
print("Значение y =", y)
print("Значение b =", b)


print("Целая часть значения b =", int(b))