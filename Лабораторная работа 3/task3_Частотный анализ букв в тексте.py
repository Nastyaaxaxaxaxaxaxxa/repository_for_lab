# TODO  Напишите функцию count_letters
def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 1
    return letter_counts  # Возвращает словарь в котором только буквы нижнего регистра.


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_counts):
    total_letters = sum(letter_counts.values())
    letter_frequencies = {}
    for letter, count in letter_counts.items():
        frequency = count / total_letters
        letter_frequencies[letter] = frequency
    return letter_frequencies  # Возвращает словарь, где буква используется как ключ, а ее частота как значение.


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letter_counts = count_letters(main_str)
letter_frequencies = calculate_frequency(letter_counts)

# TODO Распечатайте в столбик букву и её частоту в тексте
for let, freq in letter_frequencies.items():
    print(f"{let}: {freq:.2f}")
