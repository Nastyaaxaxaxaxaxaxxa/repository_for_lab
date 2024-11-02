# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group1, participants_second_group1, sp=','):
    participants_first_group1 = participants_first_group1.split(sp)
    participants_second_group1 = participants_second_group1.split(sp)
    res = list()
    for a in participants_first_group1:
        for b in participants_second_group1:
            if a == b:
               res.insert(len(res) - 1, a)
    res.sort()
    return res

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '/'))
participants_first_group = "Иванов/Петров/Сидоров"
participants_second_group = "Петров/Сидоров/Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '/'))

