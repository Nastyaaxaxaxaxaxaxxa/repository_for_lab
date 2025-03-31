import json


filename = 'input.json'
with open(filename) as file:
    data = json.load(file)


# TODO решите задачу
def task() -> float:
    res = 0
    for i in data:
        if "score" in i and "weight" in i:  # Проверка наличия ключей
            res += i["score"] * i["weight"]
        else:
            print(f"Предупреждение: Отсутствует ключ 'score' или 'weight' в словаре: {i}.  Пропускаем словарь.")
    return round(res, 3)


print(task())


