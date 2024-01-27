"""Произвольные системы счисления"""

""" Переводим из шестнадцатеричной в десятичную систему счисления"""


def hex2int(hex_str):
    decimal_result = 0
    base = 0

    for i in reversed(hex_str):
        decimal_result += int(i, 16) * (16 ** base)
        base += 1

    return decimal_result


""" Переводим из десятичной в шестнадцатеричную систему счисления"""


def int2hex(decimal_num):
    hex_result = ''

    while decimal_num > 0:
        hex_digit = hex(decimal_num % 16)[2:]
        hex_result = hex_digit + hex_result
        decimal_num //= 16

    return hex_result


""" Проверяем допустимый диапазон систем счисления"""


def is_valid_base(base):
    if 2 <= base <= 16:
        return True
    else:
        print("Допустимый диапазон систем счисления: от 2 до 16.")
        print("Выходим...")
        quit()
        return False


""" Переводим число из десятичной системы в произвольную"""


# @param num – число в десятичной системе для преобразования
# @param new_base – основание для выходного результата


def dec2n(num, new_base):
    # Формируем представление числа в новой системе счисления, сохраняя в result
    result = ''
    q = num

    # Первый запуск тела будущего цикла
    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    # Продолжаем цикл пока q не станет равен нулю
    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

    return result


""" Переводим число из произвольной системы в десятичную"""


# @param num – число в системе по основанию b, сохраненное в виде строки
# @param b – основание преобразуемого числа


def n2dec(num, b):
    decimal = 0

    # Обрабатываем каждую цифру по основанию b
    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])

    return decimal


def main():
    from_base = int(input("Исходная система счисления (2–16): "))
    from_num = input("Введите число по этому основанию: ")

    # Преобразуем в десятичное число и отображаем результат
    dec = n2dec(from_num, from_base)
    print('Результат: %d по основанию 10.' % dec)

    # Преобразуем в число с новым основанием и отображаем результат
    to_base = int(input('Введите требуемую систему счисления (2–16): '))

    to_num = dec2n(dec, to_base)
    print("Результат: %s по основанию %d." % (to_num, to_base))


if __name__ == '__main__':
    main()
