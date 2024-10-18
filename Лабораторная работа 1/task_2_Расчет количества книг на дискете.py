# TODO Найдите количество книг, которое можно разместить на дискете

disk_value = 1.44
num_of_pages = 100
num_of_lines = 50
symbol = 25
character_storage = 4

disk_value_kb = disk_value * 1024  # объем диска в килобайтах
disk_value_b = disk_value_kb * 1024  # объем диска в байтах
characters_in_the_book = symbol*num_of_lines*num_of_pages  # количсетво символов в книге
byte = characters_in_the_book * 4  # количсевто байт в одной книге
quantity = round(disk_value_b // byte)

print("Количество книг, помещающихся на дискету:", quantity)
