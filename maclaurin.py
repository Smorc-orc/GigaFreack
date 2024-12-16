def ch_maclaurin(x, terms=100):
    """Вычисляет гиперболический косинус с использованием ряда Маклорена."""
    result = 0.0
    factorial = 1.0
    for n in range(terms):
        if n > 0:
            factorial *= (2 * n - 1) * (2 * n)
        result += (x ** (2 * n)) / factorial
    print(f"Приближенное значение ch({x}) = {result}")


def ln_one_minus_x_maclaurin(x, terms=100):
    """Вычисляет ln(1 - x) с использованием ряда Маклорена."""
    if x > 1 or x <= -1:
        raise ValueError("x должен быть в интервале (-1, 1] для сходимости ряда.")
    result = 0.0
    for n in range(1, terms + 1):
        result += x ** n / n  # Суммируем члены ряда
    return print(f"Приближенное значение ln(1 - {x}) = {-result}")


def arctan_maclaurin(x, terms=100):
    """Вычисляет arctan(x) с использованием ряда Маклорена."""
    if x < -1 or x > 1:
        raise ValueError("x должен быть в интервале [-1, 1].")
    result = 0.0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)  # Вычисляем текущий член ряда
        result += term
    print(f"Приближенное значение arctan({x}) = {result}")
