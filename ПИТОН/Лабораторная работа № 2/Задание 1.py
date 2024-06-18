def main():
    name = input("Как Вас зовут? ")

    print(f"Добрый день, {name}!")

    college_name = input("Укажите названия техникума: ")

    group_number = input("Укажите номер вашей группы: ")

    print(f"Вы обучаетесь в образовательной организации {college_name} в группе {group_number}")

    programming_language = input("Какой язык программирования вы начинаете изучать? ")

    print(f"{name}, желаем Вам успешного обучения программированию на языке {programming_language}")


if __name__ == "__main__":
    main()