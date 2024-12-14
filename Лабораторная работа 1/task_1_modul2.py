import doctest
# TODO Написать 3 класса с документацией и аннотацией типов


class Cat:
    def __init__(self, color: str, age: int, name: str):
        """
        Создание и подготовка к работе объекта "Кошка"

        :param color: цвет шерсти
        :param age: возраст кошки
        :param name: имя кошки
        :raises ValueError: если возраст кошки отрицателен

        Примеры:
        >>> cat = Cat("рыжий", 5, "Персик" )  # инициализация экземпляра класса
        """
        if age < 0:
            raise ValueError("Возраст кошки не может быть отрицательным числом")
        self.color = color
        self.age = age
        self.name = name

    def speak(self) -> str:
        """
        Метод, который описывает звук, который издает кошка

        :return: строка с описанием звука который издает кошка

        Примеры:
        >>> cat = Cat("рыжий", 5, "Персик")
        >>> cat.speak()
        'meow-meow-meow'
        """
        return "meow-meow-meow"

    def play(self) -> str:
        """
        Метод, который описывает, как кошка играет.

        :return: строка с описанием игры.

        >>> cat = Cat("рыжий", 5, "Персик")
        >>> cat.play()
        'Кошка играет с мячиком.'
        """
        return "Кошка играет с мячиком."


class Car:
    def __init__(self, color: str, year: int, brand: str):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param color: цвет машины
        :param year: год выпуска
        :param brand: марка машины
        :raises ValueError: год выпуска автомобиля не может быть больше текущего

        Примеры:
        >>> car = Car("black", 2020, "BMW" )  # инициализация экземпляра класса
        """
        if year > 2024:
            raise ValueError("год выпуска автомобиля не может быть больше текущего")
        self.color = color
        self.year = year
        self.brand = brand

    def service(self) -> str:
        """
        Метод, который описывает проведение обслуживания автомобиля

       :return: строка с описанием обслуживания

        Примеры:
        >>> car = Car("black", 2020, "BMW" )
        >>> car.service()
        'Автомобиль прошел техобслуживание'
        """
        return "Автомобиль прошел техобслуживание"

    def change_tires(self) -> str:
        """
        Метод, который описывает смену шин на автомобиле

        :return: строка с описанием действия

       >>> car = Car("black", 2020, "BMW" )
       >>> car.change_tires()
       'Шины автомобиля были заменены.'
        """
        return "Шины автомобиля были заменены."


class Student:
    def __init__(self, name: str, specialization: str, course: int):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: имя студента
        :param specialization: специальность обучения
        :param course: номер курса
        :raises ValueError: если курс меньше 1 или возраст меньше 18 лет
        :raises TypeError: если курс или возраст не являются целыми числами

        Примеры:
        >>> stud = Student("Данил","Программирование", 3)  # инициализация экземпляра класса
        """
        if not isinstance(course, int):
            raise TypeError("Курс должен быть целым числом")
        if course < 1:
            raise ValueError("Курс не может быть меньше первого")

        self.name = name
        self.specialization = specialization
        self.course = course

    def take_exam(self, subject: str, grade: int) -> str:
        """
        Метод, который описывает как студент сдает экзамен

        :param subject: предмет, по которому сдается экзамен
        :param grade: оценка, полученная на экзамене
        :return: строка с результатом экзамена

        Примеры:
        >>> stud = Student("Данил","Программиование", 3)
        >>> stud.take_exam("математика", 5)
        'Данил сдал экзамен по предмету математика с оценкой 5'
        """
        if grade < 0 or grade > 5:
            return "Оценка должна быть в пределах от 0 до 5"
        return f"{self.name} сдал экзамен по предмету {subject} с оценкой {grade}"

    def get_name(self) -> str:
        """
        Получить имя студента.

        :return: имя студента

        Пример:
        >>> student = Student("Данил", "Программиование", 3)
        >>> student.get_name()
        'Данил'
        """
        return self.name


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
pass
