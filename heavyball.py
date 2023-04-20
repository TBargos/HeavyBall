import math  # нужен для вычисления тригонометрических функций
import pprint  # для адекватного вывода словаря с результатами


# Уравнение функции
def equation_func(x: int | float) -> float:
    result: float = x**3 - 2.2 * x**2 - 1.7 * math.atan(0.8 * x)
    return result


# Поиск экстремумов
def find_x_extra(x_val: list[float | int]) -> list[float | int]:
    x_min_max: list[float | int] = []
    # Сначала находим абсолютно все точки перегиба
    for i in range(len(x_val)):
        if ((i + 1) < len(x_val)) and ((i - 1) >= 0):
            if (equation_func(x_val[i]) - equation_func(x_val[i-1]))\
            * (equation_func(x_val[i+1]) - equation_func(x_val[i])) < 0:
                x_min_max.append(x_val[i])
    # Пересборка так, чтобы остались только максимум и минимум функции
    x_min_max = [min(x_min_max), max(x_min_max)]
    return x_min_max


# Метод тяжёлого шарика
def heavy_ball(x_min_max: list[int | float]) -> list[dict]:
    eps: float = .0001  # Заданная точность
    # Прочие переменные
    h: int | float
    d: int | float
    result: list[dict[str, int | float]] = []

    # Цикл позволяет перебрать два экстремума как значения листа, но с использованием индекса
    for i in range(len(x_min_max)):
        x: int | float = x_min_max[i]
        h = .2
        d = abs(h)
        n: int = 0  # Счётчик шагов
        # Для каждого экстремума нужно разное сравнение, создадим анонимную функцию или лямбда-функцию
        if x == min(x_min_max):
            comp = lambda a, b: a < b
        elif x == max(x_min_max):
            comp = lambda a, b: a > b
        # Центральный цикл
        while d > eps:
            if n != 0:  # Вычисление промежуточных переменных начинается со второго шага, не с первого
                x += h
                h = h if comp(equation_func(x - h), equation_func(x)) else -1*h/2  # Условное присвоение в одну строку
                d = abs(h)
            # Если нужно отследить промежуточные значения всех переменных
            # print("n =", n+1, "\tx =", x, "\tF(x) =", equation_func(x), "\th =", h, "\td =", d)
            n += 1
        else:
            # print("-"*160)
            n -= 1

        # Словарь для удобного вывода через pprint.pprint
        result.append({
            "n": n,
            "x": x,
            "F(x)": equation_func(x),
            "h": h,
            "d": d
        })
    return result


# Создание листа значений x
x_values: list[float] = []
for i in range(-10, 32, 2):  # числа в 10 раз больше, т.к. range не принимает float
    x_values.append(i / 10)

x_min_max = find_x_extra(x_values)  # Нахождение точек перегиба
heavy_ball_result = heavy_ball(x_min_max)  #  Уточнение экстремумов методом Тяжёлого шарика
pprint.pprint(heavy_ball_result)
