numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_left = sum(numbers[0:4])  # список до пропущенного числа
len_numbers = len(numbers)  # длина всего списка
sum_right = sum(numbers[5:len_numbers+1])  # список после пропущенного числа
average = (sum_right+sum_left)/len_numbers  # среднее арифметическое
numbers[4] = average  #

print("Измененный список:", numbers)
