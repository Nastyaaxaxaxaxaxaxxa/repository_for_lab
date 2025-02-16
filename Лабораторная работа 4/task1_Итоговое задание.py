if __name__ == "__main__":
    class Employee:
        """
        Базовый класс для представления информации о работнике.
            _salary (int): Заработная плата работника. Сделан непубличным, так как может
                           быть необходимо контролировать изменение зарплаты через метод.
        """
        def __init__(self, name: str, salary: int):
            """
            Инициализирует объект Employee.
                name (str): Имя работника.
                salary (int): Заработная плата работника.
            """
            self.name = name
            self._salary = salary

        def get_salary(self) -> int:
            """Возвращает текущую зарплату работника."""
            return self._salary

        def __str__(self) -> str:
            """Возвращает строковое представление объекта Employee."""
            return f'Имя работника: {self.name}'

        def __repr__(self) -> str:
            """Возвращает строковое представление объекта Employee для отладки."""
            return f'{self.__class__.__name__}(name={self.name!r}, salary={self._salary!r})'

        def give_raise(self, amount: int) -> None:
            """Увеличивает зарплату работника.
                amount (int): Сумма прибавки к зарплате.
            """
            self._salary += amount
            print(f"{self.name} получил повышение на {amount}. Новая зарплата: {self._salary}")

    class Manager(Employee):
        """Класс для представления информации о менеджере."""
        def __init__(self, name: str, salary: int, department: str):
            """
            Инициализирует объект Manager.
                name (str): Имя менеджера.
                salary (int): Зарплата менеджера.
                department (str): Отдел, которым управляет менеджер.
            """
            super().__init__(name, salary)
            self.department = department

        def __str__(self) -> str:
            """Возвращает строку с именем менеджера и названием отдела. Переопределен,
            чтобы включить информацию об отделе."""
            return f'{super().__str__()} (Отдел: {self.department})'

        def manage_project(self, project_name: str) -> None:
            """
            Возвращает проект, которым управляет менеджер.
            project_name (str): Название проекта.
            """
            print(f'Менеджер {self.name} управляет проектом "{project_name}" в отделе "{self.department}"')

        def give_raise(self, amount: int) -> None:
            """
            Перегруженный метод give_raise для менеджеров. Менеджеры получают
            большую прибавку, чем обычные сотрудники.
                amount (int): Сумма прибавки к зарплате.
            """
            super().give_raise(amount * 1.2)  # Увеличение прибавки на 20%

    class Engineer(Employee):
        """Класс для представления информации об инженере."""
        def __init__(self, name: str, salary: int, programming_language: str):
            """
            Инициализирует объект Engineer.
                name (str): Имя инженера.
                salary (int): Зарплата инженера.
                programming_language (str): Язык программирования, который использует инженер.
            """
            super().__init__(name, salary)
            self.programming_language = programming_language

        def __str__(self) -> str:
            """
            Возвращает строку с именем инженера и языком программирования.  Переопределен,
            чтобы включить информацию о языке программирования.
            """
            return f'{super().__str__()} (Язык программирования: {self.programming_language})'

        def code(self, task: str) -> None:
            """
            Возвращает то, для какой задачи инженер пишет код.
                task (str): Задача.
            """
            print(f'Инженер {self.name} пишет код на {self.programming_language} для задачи: {task}')

        def get_salary(self) -> int:
            """
            Перегруженный метод get_salary для инженеров. Перегружен, потому что
            необходимо добавить бонус к зарплате инженера
                int: Зарплата инженера с учетом бонуса.
            """
            return int(self._salary * 1.1)  # Для инженеров бонус 10%

        # Примеры использования
    employee = Employee("Иван Петров", 50000)
    print(employee)
    #  print(repr(employee))
    employee.give_raise(5000)

    manager = Manager("Екатерина Иванова", 80000, "Закупка материалов")
    print(manager)
    #  print(repr(manager))
    manager.manage_project("Проект№2")
    manager.give_raise(10000)

    engineer = Engineer("Данил Цветочкин", 70000, "Python")
    print(engineer)
    #  print(repr(engineer))
    engineer.code("Внедрения новой разработки")
    print(f"Зарплата инженера с бонусом: {engineer.get_salary()}")
