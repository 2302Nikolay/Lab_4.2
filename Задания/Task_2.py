class ListPerson:
    MAX_SIZE = 5

    def __init__(self):
        self.persons = []
        self.zodiac = [
            {"name": "Овен", "start_date": (3, 21), "end_date": (4, 19)},
            {"name": "Телец", "start_date": (4, 20), "end_date": (5, 20)},
            {"name": "Близнецы", "start_date": (5, 21), "end_date": (6, 20)},
            {"name": "Рак", "start_date": (6, 21), "end_date": (7, 22)},
            {"name": "Лев", "start_date": (7, 23), "end_date": (8, 22)},
            {"name": "Дева", "start_date": (8, 23), "end_date": (9, 22)},
            {"name": "Весы", "start_date": (9, 23), "end_date": (10, 22)},
            {"name": "Скорпион", "start_date": (10, 23), "end_date": (11, 21)},
            {"name": "Стрелец", "start_date": (11, 22), "end_date": (12, 21)},
            {"name": "Козерог", "start_date": (12, 22), "end_date": (1, 19)},
            {"name": "Водолей", "start_date": (1, 20), "end_date": (2, 18)},
            {"name": "Рыбы", "start_date": (2, 19), "end_date": (3, 20)},
        ]

    def get_person_by_last_name(self, l_name):
        for pers in self.persons:
            if pers["last_name"] == l_name:
                return pers
        return None  # Фамилия не найдена, карточка не доступна

    def merge_card_indexes(self, other_card_indexes):
        merged_persons = []
        for pers in self.persons + other_card_indexes:
            if pers not in merged_persons:
                merged_persons.append(pers)
        return merged_persons

    def intersect_card_indexes(self, other_card_indexes):
        intersected_persons = []
        for pers in self.persons:
            if pers in other_card_indexes:
                intersected_persons.append(pers)
        return intersected_persons

    def difference_card_indexes(self, other_card_indexes):
        difference_persons = []
        for pers in self.persons:
            if pers not in other_card_indexes:
                difference_persons.append(pers)
        return difference_persons

    def get_zodiac_sign(self, l_name):
        pers = self.get_person_by_last_name(l_name)
        if pers:
            birth_date = pers["birth_date"]
            for sign in self.zodiac:
                start_date = sign["start_date"]
                end_date = sign["end_date"]
                if (
                    (start_date[0] < birth_date[0] < end_date[0])
                    or (
                        start_date[0] == birth_date[0]
                        and birth_date[1] >= start_date[1]
                    )
                    or (end_date[0] == birth_date[0] and birth_date[1] <= end_date[1])
                ):
                    return sign["name"]
        return None  # Фамилия не найдена или дата рождения не указана, знак зодиака не определен

    def __delitem__(self, key):
        for pers in self.persons:
            if pers["last_name"] == key:
                self.persons.remove(pers)
            else:
                raise KeyError("Данного пользователя нет в списке")

    def __getitem__(self, item: str):
        return self.get_person_by_last_name(item)

    def __setitem__(self, key, value):
        for pers in self.persons:
            if pers["last_name"] == key:
                raise ValueError()  # Фамилия уже существует, карточка не добавлена
            elif len(self.persons) > self.MAX_SIZE:
                raise ValueError("Больше невозможно добавить пользователей")
        self.persons.append({"last_name": key, "birth_date": value})
        print(f"Пользователь {key} успешно добавлен")  # Карточка успешно добавлена


if __name__ == "__main__":
    list_person = ListPerson()

    print("\nВыберите действие:")
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("3. Вывести список пользователей")
    print("4. Выйти")
    print("5. Узнать знак зодиака по имени пользователя")

    while True:
        choice = input("Введите номер действия: ")

        if choice == "1":
            last_name = input("Введите фамилию пользователя: ")
            birth_date = input("Введите дату рождения пользователя (в формате mm.dd): ")
            birth_date = tuple(map(int, birth_date.split(".")))

            list_person[last_name] = birth_date

        elif choice == "2":
            last_name = input("Введите имя пользователя, которого хотите удалить: ")
            # Ваша реализация удаления пользователя
            del list_person[last_name]

        elif choice == "3":
            for person in list_person.persons:
                print(person)

        elif choice == "4":
            break

        elif choice == "5":
            name = input("Введите имя: ")
            print(list_person.get_zodiac_sign(name))

        else:
            print("Некорректный выбор. Попробуйте снова.")
