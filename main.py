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
importance = [
    'важно',
    'средне',
    'важно',
    'важно',
    'неважно',
]
urgency = [
    'срочно',
    'не срочно',
    'срочно',
    'средне',
    'не срочно',
]
done = [
    False,
    False,
    False,
    False,
    False,
]

print("Добро пожаловать в менеджер задач", "", "ЗАДАЧИ", sep="\n")
for i in range(len(texts)):
    if done[i]:
        done_step = u'\u2713'
    else:
        done_step = u'\u2610'
    print(f"{i + 1} {texts[i]} | {categories[i]} | {importance[i]} | {urgency[i]} | {done_step}")

command = input("Введите команду: ")
while command != "выход":
    if command == "добавить":
        new_task = input("Введите текст новой задачи: ")
        new_task_ctgr = input("Введите категорию: ")

        # Ограничиваем ввод данных важности данными из этой графы
        new_importance = input("Введите важность выполнения задачи: ")
        while not (new_importance in importance):
            print("Недопустимое значение!")
            new_importance = input("Введите важность выполнения задачи: ")

        # Ограничиваем ввод данных срочности данными из этой графы
        new_urgency = input("Введите срочность выполнения задачи: ")
        while not (new_urgency in urgency):
            print("Недопустимое значение!")
            new_urgency = input("Введите срочность выполнения задачи: ")

        texts.append(new_task)
        categories.append(new_task_ctgr)
        importance.append(new_importance)
        urgency.append(new_urgency)
        done.append(False)
    elif command == "изменить":
        index = int(input("Введите номер задачи для редактирования ")) - 1
        if 0 <= index < len(texts):
            pole = input("Какое поле редактируем? ")
            if pole == "текст":
                texts[index] = input("Введите текст изменяемой задачи: ")
            elif pole == "категория":
                categories[index] = input("Введите новую категорию: ")
            elif pole == "важность":
                # Ограничиваем ввод данных важности данными из этой графы
                new_importance = input("Введите новую важность выполнения задачи: ")
                while not (new_importance in importance):
                    print("Недопустимое значение!")
                    new_importance = input("Введите новую важность выполнения задачи: ")
                importance[index] = new_importance
            elif pole == "срочность":
                # Ограничиваем ввод данных важности данными из этой графы
                new_urgency = input("Введите новую срочность выполнения задачи: ")
                while not (new_urgency in urgency):
                    print("Недопустимое значение!")
                    new_urgency = input("Введите новую срочность выполнения задачи: ")
                urgency[index] = new_urgency

            elif pole == "отмена":
                print("Отмена")
            else:
                print("Такого поля нет!")
        else:
            print("Нет такого номера")
    elif command == "пометить":
        index = int(input("Введите номер задачи: ")) - 1
        if 0 <= index < len(texts):
            if done[index]:
                done[index] = False
                print(f"Задача {texts[index]} помечена как не выполнена!")
            else:
                done[index] = True
                print(f"Задача {texts[index]} помечена как выполнена!")
        else:
            print("Нет такой задачи!")
    elif command == "удалить":
        index = int(input("Введите номера задачи, которую хотите удалить: ")) - 1
        if 0 <= index < len(texts):
            texts.pop(index)
            categories.pop(index)
            importance.pop(index)
            urgency.pop(index)
            done.pop(index)
        else:
            print("Такого номера нету")
    elif command == "фильтр":
        pole = input("По какому полю фильтруем? ")
        if pole == "категория":
            category = input("Ведите категорию: ")
            print(f"Задачи с категорией ' {category} '\n")
            if category in categories:
                for i in range(len(texts)):
                    if categories[i] == category:
                        if done[i]:
                            done_step = u'\u2713'
                        else:
                            done_step = u'\u2610'
                        print(f"{i + 1} {texts[i]} | {categories[i]} | {importance[i]} | {urgency[i]} | {done_step}")
                print()
            else:
                print("отсутствуют")
                print()

        elif pole == "важность":
            important = input("Ведите важность: ")
            print(f"Задачи с важностью ' {important} '\n")
            if important in importance:
                for i in range(len(texts)):
                    if importance[i] == important:
                        if done[i]:
                            done_step = u'\u2713'
                        else:
                            done_step = u'\u2610'
                        print(f"{i + 1} {texts[i]} | {categories[i]} | {importance[i]} | {urgency[i]} | {done_step}")
                print()
            else:
                print("отсутствуют")
                print()

        elif pole == "срочность":
            urgent = input("Ведите срочность: ")
            print(f"Задачи с срочностью ' {urgent} '\n")
            if urgent in urgency:
                for i in range(len(texts)):
                    if urgency[i] == urgent:
                        if done[i]:
                            done_step = u'\u2713'
                        else:
                            done_step = u'\u2610'
                        print(f"{i + 1} {texts[i]} | {categories[i]} | {importance[i]} | {urgency[i]} | {done_step}")
                print()
            else:
                print("отсутствуют")
                print()

        else:
            print("Неверное поле фильтрации")

    elif command == "вывести":
        print("ЗАДАЧИ")
        for i in range(len(texts)):
            if done[i]:
                done_step = u'\u2713'
            else:
                done_step = u'\u2610'
            print(f"{i + 1} {texts[i]} | {categories[i]} | {importance[i]} | {urgency[i]} | {done_step}")

    else:
        print("Неизвестная команда")

    command = input("Введите команду: ")

print("Менеджер задач выключен!!!")
