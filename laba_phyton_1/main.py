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

    def to_dict(self):
        return {
            "age": self.__age,
            "hours": self.__hours,
            "wage": self.__wage,
            "ticket": self.__ticket,
            "carousel": self.__carousel
        }


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

    def to_dict(self):
        return {
            "age": self.__age,
            "height": self.__height,
            "weight": self.__weight,
            "ticket": self.__ticket
        }

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
    data_to_save = {name: item.to_dict() for name, item in data.items()}
    with open(filename, 'w') as file:
        json.dump(data_to_save, file, indent=4)


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



def main():

    workers_data = {}
    visitors_data = {}


    while True:
        print(f"Выберите опцию:")
        print("1. Добавть нового работника")
        print("2. Добавть нового посетителя")
        print("3. Загрузить данные работника")
        print("4. Загрузить данные посетителя")
        print("5. Выход")

        choice = input("Укажите номер опции:")

        if choice == '1':

            name = input("Введите имя работника: ")
            new_worker = Create_Worker()
            workers_data[name] = new_worker.to_dict()
            workers_data[name] = new_worker
            write_data_to_json(workers_data, "workers_data.json")

            while True:
                print("1. Расчитать ЗП работника")
                print("2. Показать данные")
                print("3. Сохранить данные")
                print("4. Выход")
                other_choice = input("Укажите номер опции:")

                if other_choice == '1':
                    name = input("Введите имя работника: ")
                    if name in workers_data:
                        wage = new_worker.Calculate_Wage()
                        print(wage)

                elif other_choice == '2':
                    name = input("Введите имя работника: ")
                    if name in workers_data:
                        worker = workers_data[name]
                        worker.Display_Info()
                    else:
                        print("Нет данных о человеке с таким именем.")

                elif other_choice == '3':
                    workers_data[name] = new_worker
                    write_data_to_json(workers_data, "worker_data.json")

                elif other_choice == '4':
                    break
                else:
                    print("Ошибка! Повторите выбор")


##----------------------------------------------------------------------------------------
        elif choice == '2':
            name = input("Введите имя посетителя: ")
            new_visitor = Create_Visitor()
            visitors_data[name] = new_visitor
            print(f"Новый посетитель добавлен!")

            while True:
                print("1. Узнать стоимость")
                print("2. Показать данные")
                print("3. Сохранить данные")
                print("4. Выход")
                other_choice = input("Укажите номер опции:")

                if other_choice == '1':
                    discount = new_visitor.Discount()
                    print(discount)

                elif other_choice == '2':
                    name = input("Введите имя посетителя: ")
                    if name in visitors_data:
                        visitor = visitors_data[name]
                        visitor.Display_Info()
                    else:
                        print("Нет данных о человеке с таким именем.")

                elif other_choice == '3':
                    visitors_data[name] = new_visitor
                    write_data_to_json(visitors_data, "visitors_data.json")

                elif other_choice == '4':
                    break
                else:
                    print("Ошибка! Повторите выбор")


    ##----------------------------------------------------------------------------------------
        elif choice == '3':
            name = input("Введите имя работника: ")
            saved_worker_data = read_data_from_json("saved_worker_data.json")

            if name in saved_worker_data:
                print(f"Данные сотрудника загружены!")
                saved_worker_data = Worker.from_dict(saved_worker_data[name])

            while True:
                print("1. Рассчитать ЗП работника")
                print("2. Показать данные")
                print("3. Выход")
                other_choice = input("Укажите номер опции:")

                if other_choice == '1':
                    worker = saved_worker_data
                    wage = worker.Calculate_Wage()
                    print(wage)

                elif other_choice == '2':
                    worker = saved_worker_data
                    worker.Display_Info()

                elif other_choice == '3':
                    break
                else:
                    print("Ошибка! Повторите выбор")


    ##----------------------------------------------------------------------------------------
        elif choice == '4':
            name = input("Введите имя посетителя: ")
            saved_visitor_data = read_data_from_json("saved_visitor_data.json")

            if name in saved_visitor_data:
                print(f"Данные посетителя загружены!")
                saved_visitor_data = Visitor.from_dict(saved_visitor_data[name])
                visitor = saved_visitor_data
            while True:
                    print("1. Проверить, есть ли скидка")
                    print("2. Проверить билет")
                    print("3. Проверить вес и рост")
                    print("4. Показать данные")
                    print("5. Выход")
                    other_choice = input("Укажите номер опции:")

                    if other_choice == '1':
                        visitor.Discount()

                    elif other_choice == '2':
                        visitor.Check_ticket()

                    elif other_choice == '3':
                        visitor.Check_Weight_Height()

                    elif other_choice == '4':
                        visitor.Display_Info()

                    elif other_choice == '5':
                        break

        elif choice == '5':
            exit()

        else:
            print("Ошибка! Повторите выбор")

if __name__ == "__main__":
    main()

