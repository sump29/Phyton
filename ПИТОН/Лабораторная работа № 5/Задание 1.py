while True:

    num = float(input("Введите число (для завершения введите 0): "))


    if num == 0:
        break


    inverse_num = 1 / num
    print("Обратное значение числа {}: {}".format(num, inverse_num))