salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0
actual_spend = spend

# Цикл будет повторяться 10 раз
for month in range(months):
    money_capital += actual_spend - salary  # К подушке безопасности будет добавлена разница м/у расходами и зп
    actual_spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
