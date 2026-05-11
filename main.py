import importlib
import shlex
import classes as cl


# ---------- Парсеры ----------

def parse_natural(s: str) -> cl.natural:
    return cl.natural([int(ch) for ch in s])


def parse_integer(s: str) -> cl.integer:
    if s.startswith("-"):
        return cl.integer(1, parse_natural(s[1:]))
    if s.startswith("+"):
        return cl.integer(0, parse_natural(s[1:]))
    return cl.integer(0, parse_natural(s))


def parse_rational(s: str) -> cl.rational:
    if "/" in s:
        num, den = s.split("/")
        return cl.rational(parse_integer(num), parse_natural(den))
    return cl.rational(parse_integer(s), cl.natural([1]))


import re
import classes as cl


def parse_polynom(expr: str) -> cl.polynom:
    expr = expr.replace(" ", "")
    expr = expr.replace("-", "+-")

    if expr.startswith("+"):
        expr = expr[1:]

    terms = expr.split("+")

    parsed = []

    max_power = 0

    for term in terms:
        if term == "":
            continue

        coef = "1"
        power = 0

        # x^k
        if "x^" in term:
            parts = term.split("x^")

            coef = parts[0]
            power = int(parts[1])

        # x
        elif "x" in term:
            parts = term.split("x")

            coef = parts[0]
            power = 1

        # число
        else:
            coef = term
            power = 0

        # коэффициенты
        if coef == "":
            coef = "1"

        if coef == "-":
            coef = "-1"

        # рациональный коэффициент
        if "/" in coef:
            num, den = coef.split("/")

            rat = cl.rational(
                parse_integer(num),
                parse_natural(den)
            )
        else:
            rat = cl.rational(
                parse_integer(coef),
                cl.natural([1])
            )

        parsed.append((power, rat))

        max_power = max(max_power, power)

    # создаём все коэффициенты нулями
    zero = cl.rational(
        cl.integer(0, cl.natural([0])),
        cl.natural([1])
    )

    coef = [zero for _ in range(max_power + 1)]

    # раскладываем коэффициенты
    for power, rat in parsed:
        index = max_power - power
        coef[index] = rat

    return cl.polynom(coef)


def parse_digit(s: str) -> int:
    d = int(s)
    if d < 0 or d > 9:
        raise ValueError("Цифра должна быть от 0 до 9")
    return d


def parse_int(s: str) -> int:
    return int(s)


# ---------- Вывод ----------

def natural_to_str(x: cl.natural):
    return "".join(map(str, x.data))


def integer_to_str(x: cl.integer):
    sign = "-" if x.sign == 1 else ""
    return sign + natural_to_str(x.data)


def rational_to_str(x: cl.rational):
    num = integer_to_str(x.numerator)
    den = natural_to_str(x.denominator)

    if den == "1":
        return num

    return f"{num}/{den}"


def polynom_to_str(p: cl.polynom):
    return str(p)


def result_to_str(x):
    if x is None:
        return "None"

    if isinstance(x, cl.natural):
        return natural_to_str(x)

    if isinstance(x, cl.integer):
        return integer_to_str(x)

    if isinstance(x, cl.rational):
        return rational_to_str(x)

    if isinstance(x, cl.polynom):
        return polynom_to_str(x)

    return str(x)


# ---------- Таблица функций ----------

FUNCTIONS = {
    # N
    "COM_NN_D": ("COM_NN_D", ["N", "N"]),
    "NZER_N_B": ("NZER_N_B", ["N"]),
    "ADD_1N_N": ("ADD_1N_N", ["N"]),
    "ADD_NN_N": ("ADD_NN_N", ["N", "N"]),
    "SUB_NN_N": ("SUB_NN_N", ["N", "N"]),
    "MUL_ND_N": ("MUL_ND_N", ["N", "D"]),
    "MUL_Nk_N": ("MUL_Nk_N", ["N", "INT"]),
    "MUL_NN_N": ("MUL_NN_N", ["N", "N"]),
    "SUB_NDN_N": ("SUB_NDN_N", ["N", "N", "D"]),
    "DIV_NN_Dk": ("DIV_NN_Dk", ["N", "N"]),
    "DIV_NN_N": ("DIV_NN_N", ["N", "N"]),
    "MOD_NN_N": ("MOD_NN_N", ["N", "N"]),
    "GCF_NN_N": ("GCF_NN_N", ["N", "N"]),
    "LCM_NN_N": ("LCM_NN_N", ["N", "N"]),

    # Z
    "ABS_Z_Z": ("ABS_Z_Z", ["Z"]),
    "SGN_Z_D": ("SGN_Z_D", ["Z"]),
    "POZ_Z_D": ("POZ_Z_D", ["Z"]),
    "MUL_ZM_Z": ("MUL_ZM_Z", ["Z"]),
    "TRANS_N_Z": ("TRANS_N_Z", ["N"]),
    "TRANS_Z_N": ("TRANS_Z_N", ["Z"]),
    "ADD_ZZ_Z": ("ADD_ZZ_Z", ["Z", "Z"]),
    "SUB_ZZ_Z": ("SUB_ZZ_Z", ["Z", "Z"]),
    "MUL_ZZ_Z": ("MUL_ZZ_Z", ["Z", "Z"]),
    "DIV_ZZ_Z": ("DIV_ZZ_Z", ["Z", "Z"]),
    "MOD_ZZ_Z": ("MOD_ZZ_Z", ["Z", "Z"]),

    # Q
    "RED_Q_Q": ("RED_Q_Q", ["Q"]),
    "INT_Q_B": ("INT_Q_B", ["Q"]),
    "TRANS_Z_Q": ("TRANS_Z_Q", ["Z"]),
    "TRANS_Q_Z": ("TRANS_Q_Z", ["Q"]),
    "ADD_QQ_Q": ("ADD_QQ_Q", ["Q", "Q"]),
    "SUB_QQ_Q": ("SUB_QQ_Q", ["Q", "Q"]),
    "MUL_QQ_Q": ("MUL_QQ_Q", ["Q", "Q"]),
    "DIV_QQ_Q": ("DIV_QQ_Q", ["Q", "Q"]),

    # P
    "ADD_PP_P": ("ADD_PP_P", ["P", "P"]),
    "SUB_PP_P": ("SUB_PP_P", ["P", "P"]),
    "MUL_PQ_P": ("MUL_PQ_P", ["P", "Q"]),
    "MUL_Pxk_P": ("MUL_Pxk_P", ["P", "INT"]),
    "LED_P_Q": ("LED_P_Q", ["P"]),
    "DEG_P_N": ("DEG_P_N", ["P"]),
    "FAC_P_Q": ("FAC_P_Q", ["P"]),
    "MUL_PP_P": ("MUL_PP_P", ["P", "P"]),
    "DIV_PP_P": ("DIV_PP_P", ["P", "P"]),
    "MOD_PP_P": ("MOD_PP_P", ["P", "P"]),
    "GCF_PP_P": ("GCF_PP_P", ["P", "P"]),
    "DER_P_P": ("DER_P_P", ["P"]),
    "NMR_P_P": ("NMR_P_P", ["P"]),
}


def parse_arg(value: str, arg_type: str):
    if arg_type == "N":
        return parse_natural(value)

    if arg_type == "Z":
        return parse_integer(value)

    if arg_type == "Q":
        return parse_rational(value)

    if arg_type == "P":
        return parse_polynom(value)

    if arg_type == "D":
        return parse_digit(value)

    if arg_type == "INT":
        return parse_int(value)

    raise ValueError(f"Неизвестный тип аргумента: {arg_type}")


def load_function(func_name: str):
    module = importlib.import_module(func_name)
    return getattr(module, func_name)


def execute_command(line: str):
    tokens = shlex.split(line)

    if not tokens:
        return

    func_name = tokens[0]

    if func_name not in FUNCTIONS:
        print("Неизвестная функция")
        return

    module_name, arg_types = FUNCTIONS[func_name]

    args_raw = tokens[1:]

    if len(args_raw) != len(arg_types):
        print(f"Ошибка: функция {func_name} ожидает {len(arg_types)} арг.")
        print(f"Типы аргументов: {arg_types}")
        return

    args = []

    for value, arg_type in zip(args_raw, arg_types):
        args.append(parse_arg(value, arg_type))

    func = load_function(module_name)
    result = func(*args)

    print(result_to_str(result))


def print_help():
    print("======== НАТУРАЛЬНЫЕ ЧИСЛА ========")

    print("COM_NN_D 123 456               - Сравнение натуральных чисел")
    print("NZER_N_B 123                  - Проверка на ноль")
    print("ADD_1N_N 999                  - Добавление 1 к натуральному числу")
    print("ADD_NN_N 123 456              - Сложение натуральных чисел")
    print("SUB_NN_N 456 123              - Вычитание натуральных чисел")
    print("MUL_ND_N 123 7                - Умножение натурального числа на цифру")
    print("MUL_Nk_N 123 5                - Умножение натурального числа на 10^k")
    print("MUL_NN_N 123 456              - Умножение натуральных чисел")
    print("SUB_NDN_N 1000 12 8           - Вычитание натурального числа и другого, умноженного на цифру")
    print("DIV_NN_Dk 9876 123            - Первая цифра деления натуральных чисел")
    print("DIV_NN_N 9876 123             - Частное от деления натуральных чисел")
    print("MOD_NN_N 9876 123             - Остаток от деления натуральных чисел")
    print("GCF_NN_N 48 18                - НОД натуральных чисел")
    print("LCM_NN_N 12 18                - НОК натуральных чисел")

    print()
    print("======== ЦЕЛЫЕ ЧИСЛА ========")

    print("ABS_Z_Z -123                  - Абсолютная величина целого числа")
    print("SGN_Z_D -123                  - Определение знака числа")
    print("POZ_Z_D -123                  - Проверка положительности числа")
    print("MUL_ZM_Z -123                 - Умножение целого числа на -1")
    print("TRANS_N_Z 123                 - Преобразование натурального в целое")
    print("TRANS_Z_N 123                 - Преобразование целого неотрицательного в натуральное")
    print("ADD_ZZ_Z -123 456             - Сложение целых чисел")
    print("SUB_ZZ_Z -123 456             - Вычитание целых чисел")
    print("MUL_ZZ_Z -12 34               - Умножение целых чисел")
    print("DIV_ZZ_Z -7 3                 - Частное от деления целых чисел")
    print("MOD_ZZ_Z -7 3                 - Остаток от деления целых чисел")

    print()
    print("======== РАЦИОНАЛЬНЫЕ ЧИСЛА ========")

    print("RED_Q_Q 6/8                   - Сокращение дроби")
    print("INT_Q_B 6/3                   - Проверка, является ли дробь целым числом")
    print("TRANS_Z_Q -123                - Преобразование целого в рациональное")
    print("TRANS_Q_Z 5/1                 - Преобразование рационального в целое")
    print("ADD_QQ_Q 1/2 3/4              - Сложение рациональных чисел")
    print("SUB_QQ_Q 1/2 3/4              - Вычитание рациональных чисел")
    print("MUL_QQ_Q 2/3 5/7              - Умножение рациональных чисел")
    print("DIV_QQ_Q 2/3 5/7              - Деление рациональных чисел")

    print()
    print("======== МНОГОЧЛЕНЫ ========")

    print('ADD_PP_P "x^2 + 3x + 2" "x + 1"          - Сложение многочленов')
    print('SUB_PP_P "x^2 + 3x + 2" "x + 1"          - Вычитание многочленов')
    print('MUL_PQ_P "x^2 + 3x + 2" 1/2              - Умножение многочлена на рациональное число')
    print('MUL_Pxk_P "x + 1" 3                      - Умножение многочлена на x^k')
    print('LED_P_Q "3x^2 + x + 1"                   - Старший коэффициент многочлена')
    print('DEG_P_N "3x^2 + x + 1"                   - Степень многочлена')
    print('FAC_P_Q "2/3x^2 + 4/5x + 6/7"           - Вынесение НОК/НОД коэффициентов')
    print('MUL_PP_P "x^2 + 3x + 2" "x + 1"          - Умножение многочленов')
    print('DIV_PP_P "x^2 + 3x + 2" "x + 1"          - Деление многочленов')
    print('MOD_PP_P "x^2 + 1" "x + 1"               - Остаток от деления многочленов')
    print('GCF_PP_P "x^2 + 3x + 2" "x^2 + 4x + 3"  - НОД многочленов')
    print('DER_P_P "3x^3 + 2x^2 + x + 5"            - Производная многочлена')
    print('NMR_P_P "x^3 - 3x + 2"                   - Удаление кратных корней')

    print()
    print("======== ФОРМАТЫ ========")

    print("123                  - Натуральное число")
    print("-123                 - Целое число")
    print("3/4                  - Рациональное число")
    print('"x^2 + 3x + 2"       - Многочлен')

    print()
    print("help                 - Показать справку")
    print("funcs                - Показать список функций")
    print("exit                 - Выход")


def main():
    print("Компьютерная алгебра")
    print("Введите help для справки.")

    while True:
        try:
            line = input(">>> ").strip()

            if line == "":
                continue

            if line == "exit":
                break

            if line == "help":
                print_help()
                continue

            if line == "funcs":
                for name in FUNCTIONS:
                    print(name)
                continue

            execute_command(line)

        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()