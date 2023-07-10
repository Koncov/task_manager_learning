texts = [
    'Побрить руку',
    'Опровергнуть теорему Пифагора',
    'Построить скворечник',
    'Посмотреть кино',
    'Сходить в магазин',
]
categories = [
    'красота',
    'работа',
    'работа',
    'хобби',
    'хобби',
]

print("Добро пожаловать в менеджер задач", "", "ЗАДАЧИ", sep="\n")

for i in range(len(texts)):
    print(f"{i + 1} {texts[i]} | {categories[i]}")

command = input("Введите команду: ")
while command != "выход":
    if command == "добавить":
        new_task = input("Введите текст новой задачи: ")
        new_task_ctgr = input("Введите категорию: ")
        texts.append(new_task)
        categories.append(new_task_ctgr)
    elif command == "изменить":
        index = int(input("Введите номер задачи для редактирования ")) - 1
        if 0 <= index < len(texts):
            pole = input("Какое поле редактирем? ")
            if pole == "текст":
                texts[index] = input("Введите текст изменяемой задачи: ")
            elif pole == "категория":
                categories[index] = input("Введите новую категорию: ")
            elif pole == "отмена":
                print("Отмена")
            else:
                print("Такого поля нет!")
        else:
            print("Нет такого номера")
    elif command == "удалить":
        index = int(input("Введите номера задачи, которую хотите удалить: ")) - 1
        if 0 <= index < len(texts):
            texts.pop(index)
            categories.pop(index)
        else:
            print("Такого номера нету")
    elif command == "фильтр":
        pole = input("По какому полю фильтруем? ")
        if pole == "категория":
            category = input("Ведите категорию: ")
            print(f"Задачи с категорией ' {category} '")
            if category in categories:
                for i in range(len(texts)):
                    if categories[i] == category:
                        print(f"{i + 1} {texts[i]} | {categories[i]}")
                print()
            else:
                print("отсутствуют")
                print()
        else:
            print("Неверное поле фильтрации")
    else:
        print("Неизвестная команда")

    print("ЗАДАЧИ")
    for i in range(len(texts)):
        print(f"{i + 1} {texts[i]} | {categories[i]}")

    command = input("Введите команду: ")

print("Менеджер задач выключен!!!")
