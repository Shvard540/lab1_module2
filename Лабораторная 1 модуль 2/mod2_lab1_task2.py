from task_1 import Calculator, Car, Tasks

if __name__ == "__main__":
 p1 = Calculator()
 p2 = Car()
 p3 = Tasks()

    try:
     p1.calc_a_p_b("100% its int",34)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     p2.new_speed(-9)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     p3.change_diff(23.5)
    except TypeError:
        print('Ошибка: неправильные данные')
