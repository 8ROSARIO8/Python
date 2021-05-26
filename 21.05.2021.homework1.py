duration = input('Введите промежуток времени в секундах:')
duration = int(duration)
minute = 60
hour = 3600
day = 86400
a_week = 604800
month = 2592000
if duration == minute:
    print('1 мин')
elif duration == hour:
    print('1 час')
elif duration == day:
    print('1 день')
elif duration == a_week:
    print('1 нед')
elif duration == month:
    print('1 мес')
elif duration < minute:
    print(duration, 'сек')
elif hour > duration > minute:
    num_sec = duration % 60
    num_min = duration // 60
    print(num_min, ' мин ', num_sec, 'сек')
elif day > duration > hour:
    num_sec = duration % 3600
    num_hour = duration // 3600
    if num_sec < minute:
        print(num_hour, ' час ', num_sec, 'сек')
    elif num_sec == minute:
        print(num_hour, ' час 1 min')
    elif num_sec > minute:
        sec = num_sec % 60
        num_min = num_sec // 60
        print(num_hour, ' час ', num_min, ' мин', sec, ' сек')
elif a_week > duration > day:
    num_sec = duration % 86400
    num_day = duration // 86400
    if num_sec == minute:
        print(num_day, ' дн 1 мин')
    elif num_sec == hour:
        print(num_day, ' дн 1 час ')
    elif num_sec < minute:
        print(num_day, ' дн ', num_sec, ' сек')
    elif hour > num_sec > minute:
        sec = num_sec % 60
        num_min = num_sec // 60
        print(num_day, ' дн ', num_min, ' мин ', sec, ' сек')
    elif day > num_sec > hour:
        sec = num_sec % 3600
        num_hour = num_sec // 3600
        if sec < minute:
            print(num_day, ' дн ', num_hour, ' час ', sec, ' сек')
        elif sec == minute:
            print(num_day, ' дн ', num_hour, ' час 1 мин')
        elif sec > minute:
            num_sec = sec % 60
            num_min = sec // 60
            print(num_day, ' дн ', num_hour, ' час ', num_min, ' мин ', num_sec, ' сек')
elif month > duration > a_week:
    num_sec = duration % 604800
    num_a_week = duration // 604800
    if num_sec == minute:
        print(num_a_week, ' нд 1 мин')
    elif num_sec == hour:
        print(num_a_week, ' нд 1 час ')
    elif num_sec == day:
        print(num_a_week, ' нд 1 дн ')
    elif num_sec < minute:
        print(num_a_week, ' нд ', num_sec, ' сек')
    elif hour > num_sec > minute:
        sec = num_sec % 60
        num_min = num_sec // 60
        print(num_a_week, ' нд ', num_min, ' мин ', sec, ' сек')
    elif day > num_sec > hour:
        sec = num_sec % 3600
        num_hour = num_sec // 3600
        if sec < minute:
            print(num_a_week, ' нд ', num_hour, ' час ', sec, ' сек')
        elif sec == minute:
            print(num_a_week, ' нд ', num_hour, ' час 1 мин')
        elif sec > minute:
            num_sec = sec % 60
            num_min = sec // 60
            print(num_a_week, ' нд ', num_hour, ' час ', num_min, ' мин ', num_sec, ' сек')
    elif a_week > num_sec > day:
        sec = num_sec % 86400
        num_day = num_sec // 86400
        if sec == minute:
            print(num_a_week, ' нд ', num_day, ' дн 1 мин')
        elif sec == hour:
            print(num_a_week, ' нд ', num_day, ' дн 1 час')
        elif sec < minute:
            print(num_a_week, ' нд ', num_day, ' дн 1 мин', sec, ' сек')
        elif hour > sec > minute:
            num_sec = sec % 60
            num_min = sec // 60
            print(num_a_week, ' нд ', num_day, ' дн ', num_min, ' мин ', num_sec, ' сек')
        elif day > sec > hour:
            num_sec = sec % 3600
            num_hour = sec // 3600
            if num_sec < minute:
                print(num_a_week, ' нд ', num_day, ' дн ', num_hour, ' час ', num_sec, ' сек')
            elif num_sec == minute:
                print(num_a_week, ' нд ', num_day, ' дн ', num_hour, ' час 1 мин')
            elif num_sec > minute:
                sec = num_sec % 60
                num_min = num_sec // 60
                print(num_a_week, ' нд ', num_day, ' дн ', num_hour, ' час ', num_min, ' мин ', sec, ' сек')
elif duration > month:
    print('Более месяца')

array_num = [number ** 3 for number in range(1, 1001, 2)]

# 2.a

sun_num = 0
for number in array_num:
    check_sum = 0
    for check_num in str(number):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        sun_num += number
print(sun_num)

# 2.b

sun_num2 = 0
for number in array_num:
    number += 17
    check_sum = 0
    for check_num in str(number):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        sun_num2 += number
print(sun_num2)

# извинете, что скопировал, просто реально не понятно, я смог сам создать массив(список) только загуглив,
# просмотрел урок ваш, так всё равно не понял, вот моё решение:

# 2

array_number = [array ** 3 for array in range(1, 1000, 2)]

sum_num = 0
sum_num1 = 0
sum_arr = 0
index = 0
index1 = 0

# 2/a

while index < len(array_number):
    sum_arr += array_number[index] % 10
    array_number[index] = array_number[index] // 10
    if sum_arr % 7 == 1:
        sum_num += array_number[index]
    index += 1
print(sum_num)

# 2/b

while index1 < len(array_number):
    array_number[index1] += 17
    sum_arr += array_number[index1] % 10
    array_number[index1] = array_number[index1] // 10
    if sum_arr % 7 == 0:
        sum_num1 += array_number[index1]
    index1 += 1
print(sum_num1)


# 3 здесь тоже хотел с инпровезировать, сделать с полной проверкой при помощи while до любого числа, но не получилось
# пришлось тоже просто скопировать, но тут всё равно просто, хотелось создать полную проверку от 0 до введённого числа.

sum_percent = input('Введите количество процентов: ')
sum_percent = int(sum_percent)
if sum_percent == 1:
    word = 'процент'
elif sum_percent <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(sum_percent, word)

# постараюсь следующнн дз сделать сам.
