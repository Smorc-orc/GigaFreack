def inpp():
    """Функция проверки и ввода переменной x"""
    while True:
        try:
            x = float(input("Введите число х: "))
            break
        except ValueError:
            print('Введены некорректные данные')
            continue

    return x
