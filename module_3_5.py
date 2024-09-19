def get_multiplied_digits(number):
    global counter # глобальный счетчик итераций рекурсии
    if counter == 0 and number == 0: # проверка на ввод одного 0
        return 0

    str_number = str(number)
    first = int(str_number[0])
    counter += 1

    if first == 0: # в случае если 0 последний
        return 1

    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

counter = 0
result = get_multiplied_digits(40203)
print(result)
