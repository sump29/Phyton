A = float(input("Введите размер стипендии (руб.): "))
B = float(input("Введите текущие расходы на проживание (руб.): "))

month = 1
total_needed = 0
while month <= 10:
  total_needed += B - A
  B *= 1.03
  month += 1

print("Необходимая сумма от родителей:", total_needed, "руб.")