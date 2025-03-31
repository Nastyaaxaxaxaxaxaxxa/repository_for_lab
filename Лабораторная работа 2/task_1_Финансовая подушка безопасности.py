money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0  # Счетчик месяцев
actual_budget = salary + money_capital  # Актуальный бюджет
actual_spend = spend  # Актуальные траты с изначальным значением заданным в условии

while actual_budget >= actual_spend:
    months += 1
    actual_budget -= actual_spend  # Вычитаем текущие расходы из бюджета
    actual_budget += salary  # Прибавляем к бюдежу зарплату
    actual_spend *= (1 + increase)  # Увеличиваем расходы на 5%

print("Количество месяцев, которое можно протянуть без долгов:", months)
