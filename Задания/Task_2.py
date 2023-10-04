class ListPerson:
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
            {"name": "Рыбы", "start_date": (2, 19), "end_date": (3, 20)}
        ]

    def add_person(self, last_name, birth_date):
        for person in self.persons:
            if person["last_name"] == last_name:
                return False  # Фамилия уже существует, карточка не добавлена
        self.persons.append({"last_name": last_name, "birth_date": birth_date})
        return True  # Карточка успешно добавлена

    def remove_person(self, last_name):
        for person in self.persons:
            if person["last_name"] == last_name:
                self.persons.remove(person)
                return True  # Карточка успешно удалена
        return False  # Фамилия не найдена, карточка не удалена

    def get_person_by_last_name(self, last_name):
        for person in self.persons:
            if person["last_name"] == last_name:
                return person
        return None  # Фамилия не найдена, карточка не доступна

    def merge_card_indexes(self, other_card_indexes):
        merged_persons = []
        for person in self.persons + other_card_indexes:
            if person not in merged_persons:
                merged_persons.append(person)
        return merged_persons

    def intersect_card_indexes(self, other_card_indexes):
        intersected_persons = []
        for person in self.persons:
            if person in other_card_indexes:
                intersected_persons.append(person)
        return intersected_persons

    def difference_card_indexes(self, other_card_indexes):
        difference_persons = []
        for person in self.persons:
            if person not in other_card_indexes:
                difference_persons.append(person)
        return difference_persons

    def get_zodiac_sign(self, last_name):
        person = self.get_person_by_last_name(last_name)
        if person:
            birth_date = person["birth_date"]
            for sign in self.zodiac:
                start_date = sign["start_date"]
                end_date = sign["end_date"]
                if (start_date[0] < birth_date[0] < end_date[0]) or (
                    start_date[0] == birth_date[0] and birth_date[1] >= start_date[1]
                ) or (
                    end_date[0] == birth_date[0] and birth_date[1] <= end_date[1]
                ):
                    return sign["name"]
        return None  # Фамилия не найдена или дата рождения не указана, знак зодиака не определен
