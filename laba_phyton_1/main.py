import json

class Entertainment_Park_Error(Exception):
    def __init__(self, ticket):
        self.ticket = ticket

    def __str__(self):
        return f'Количество билетов не может быть равно {self.ticket}, пожалуйста, укажите другое число!'

class Entertainment_Park():

    def __set__(self, price):
        self.price = 100

class Worker(Entertainment_Park):
    def __init__(self, data):
        self.__age = data["age"]
        self.__hours = data["hours"]
        self.__wage = data["wage"]
        self.__ticket = data["ticket"]
        self.__carousel = data["carousel"]


    def Calculate_Wage(self):
        self.__wage = self.__wage + (self.__hours * 50) + (self.__ticket * 15)
        return print(f"Зарплата за день: {self.__wage}")



    def Display_Info(self):
        print(f"Возраст работника: {self.__age}")
        print(f"Время смены: {self.__hours}")
        print(f"Оклад за выход на смену: {self.__wage}")
        print(f"Количество проданных билетов за смену: {self.__ticket}")
        print(f"Прикреплен к: {self.__carousel}")



    @classmethod
    def from_dict(cls, data):
        return cls(data)

class Visitor(Entertainment_Park):
    def __init__(self, age, height, weight, ticket):
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__ticket = ticket
        self.Check_ticket()
        self.Check_Weight_Height()
        self.price = 100

    def Display_Info(self):
        print(f"Age: {self.__age}")
        print(f"Height: {self.__height}")
        print(f"weight: {self.__weight}")
        print(f"Ticket: {self.__ticket}")

    def Discount(self):
        self.disc = self.__ticket * self.price
        if self.__ticket > 6:
            return print(f"У вас скидка 10%! Итоговая стоимость: {self.disc-(self.disc * 0.1)}")
        else:
            return print(f"Скидка при покупке от 6 билетов! Итоговая стоимость: {self.disc}")

    @classmethod
    def from_dict(cls, data):
        age = data.get("age")
        height = data.get("height")
        weight = data.get("weight")
        ticket = data.get("ticket")
        return cls(age, height, weight, ticket)

    def Check_ticket(self):
        if self.__ticket <= 0:
            raise Entertainment_Park_Error(self.__ticket)

    def Check_Weight_Height(self):
        if self.__height > 180:
            return print(f"Извините, для этого аттракциона ваш рост : {self.__height} не подходит!")
        elif self.__weight > 90:
            return print(f"Извините, для этого аттракциона ваш вес: {self.__weight} не подходит!")

def read_data_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def write_data_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def Create_Worker():
    age = int(input("Введите возраст работника:"))
    hours = int(input("Введите время смены работника:"))
    wage = int(input("Введите оклад за выход на смену:"))
    ticket = int(input("Укажите количество проданных билетов за смену:"))
    carousel = input("Укажите, к какой каруселе прикреплен работник: ")

    worker_data = {
        "age": age,
        "hours": hours,
        "wage": wage,
        "ticket": ticket,
        "carousel": carousel
    }

    worker = Worker.from_dict(worker_data)
    return worker

def Create_Visitor():
    age = int(input("Укажите возраст посетителя:"))
    height = int(input("Укажите рост посетителя:"))
    weight = int(input("Укажите вес поситителя:"))
    ticket = int(input("Сколько билетов вы хотите купить?"))

    visitor_data = {
        "age": age,
        "height": height,
        "weight": weight,
        "ticket": ticket,
    }

    visitor = Visitor.from_dict(visitor_data)
    return visitor



print(f"Выберите опцию:")
print("1. Добавть нового работника")
print("2. Добавть нового посетителя")
print("3. Загрузить данные работника")
print("4. Загрузить данные посетителя")


choice = input("Укажите номер опции:")

if choice == '1':
    new_worker = Create_Worker()
    print(f"Новый сотрудник добавлен!")

    print("1. Расчитать ЗП работника")
    print("2. Показать данне")
    print("3. Сохранить данные")
    print("4. Выход")
    other_choice = input("Укажите номер опции:")

    if other_choice == '1':
        new_worker.Calculate_Wage()

    elif other_choice == '2':
        new_worker.Display_Info()

    elif other_choice == '3':
        worker_data = {
            "age": new_worker._Worker__age,
            "hours": new_worker._Worker__hours,
            "wage": new_worker._Worker__wage,
            "ticket": new_worker._Worker__ticket,
            "carousel": new_worker._Worker__carousel
        }
        write_data_to_json(worker_data, "save_data_new_worker.json")

    elif other_choice == '4':
        exit()
    else:
        print("Ошибка! Повторите выбор")


elif choice == '2':
    new_visitor = Create_Visitor()
    print(f"Новый посетитель добавлен!")

    print("1. Узнать стоимость")
    print("2. Проверить билет")
    print("3. Проверить вес и рост")
    print("4. Показать данне")
    print("5. Сохранить данные")
    print("6. Выход")
    other_choice = input("Укажите номер опции:")

    if other_choice == '1':
        new_visitor.Discount()

    elif other_choice == '2':
        new_visitor.Check_ticket()

    elif other_choice == '3':
        new_visitor.Check_Weight_Height()

    elif other_choice == '4':
        new_visitor.Display_Info()


    elif other_choice == '5':
        visitor_data = {
            "age": new_visitor._Visitor__age,
            "height": new_visitor._Visitor__height,
            "weight": new_visitor._Visitor__weight,
            "ticket": new_visitor._Visitor__ticket,
        }
        write_data_to_json(visitor_data, "save_data_new_visitor.json")

    elif other_choice == '6':
        exit()
    else:
        print("Ошибка! Повторите выбор")


elif choice == '3':
    loaded_data = read_data_from_json("new_worker_data.json")
    new_worker1 = Worker.from_dict(loaded_data)
    print(f"Данные сотрудника загружены!")

    print("1. Расчитать ЗП работника")
    print("2. Показать данне")
    print("3. Выход")
    other_choice = input("Укажите номер опции:")

    if other_choice == '1':
        new_worker1.Calculate_Wage()

    elif other_choice == '2':
        new_worker1.Display_Info()

    elif other_choice == '3':
        pass
    else:
        print("Ошибка! Повторите выбор")


elif choice == '4':
    loaded_data = read_data_from_json("new_visitor_data.json")
    new_visitor1 = Visitor.from_dict(loaded_data)
    print(f"Данные посетителя загружены!")


    print("1. Проверить, есть ли скидка")
    print("2. Проверить билет")
    print("3. Проверить вес и рост")
    print("4. Показать данне")
    print("5. Выход")
    other_choice = input("Укажите номер опции:")

    if other_choice == '1':
        new_visitor1.Discount()

    elif other_choice == '2':
        new_visitor1.Check_ticket()

    elif other_choice == '3':
        new_visitor1.Check_Weight_Height()

    elif other_choice == '4':
        new_visitor1.Display_Info()

    elif other_choice == '5':
        exit()
    else:
        print("Ошибка! Повторите выбор")



