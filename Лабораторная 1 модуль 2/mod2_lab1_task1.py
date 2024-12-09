# TODO: Подробно описать три произвольных класса


class Calculator:
    def __init__(self, number1: float, number2: float):
        """

        :param number1: число 1
        :param number2: число 2

        >>> p1 = Calculator(12,23)
        """
        self.num1 = number1
        self.num2 = number2

        if not isinstance((number1 or number2), (int, float)):
            raise TypeError("число должно быть int или float")

    def calc_a_p_b(self):
        """
        выводит сумму чисел 1 и 2

        :return: сумма

        >>> p1 = Calculator(12,23)
        >>> p1.calc_a_p_b()
        """
        print(self.num1+self.num2)
        ...

    def calc_a_m_b(self):
        """
        выводит разность чисел 1 и 2

        :return: разность

        >>> p1 = Calculator(12,23)
        >>> p1.calc_a_m_b()
        """
        print(self.num1-self.num2)
        ...


class Car:
    def __init__(self, speed: float, protection = 1000):
        """

        :param speed: скорость
        :param protection: прочность

        >>> p2 = Car(100)
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("скорость должна быть int или float")
        self.speed = speed
        self.prot = protection

    def crash(self):
        """
        снижает прочность на 25%
        :return: новая прочность

        >>> p2 = Car()
        >>> p2.crash()
        >>> print(p2.prot)
        """
        self.prot *= 0.75
        ...

    def new_speed(self, s: float):
        """
        устанавливает новую скорость

        :param s: число от пользователя
        :return: новая скорость


        >>> p2 = Car()
        >>> p2.new_speed(134)
        >>> print(p2.speed)
        """
        if not isinstance(s, (int, float)):
            raise  TypeError("новая скорость должна быть int или float")
        if s < 0:
            raise ValueError("новая скорость должна быть положительной")
        self.speed = s
        ...


class Tasks:
    def __init__(self, number = 12, difficulty = 1):
        """

        :param number: кол-во
        :param difficulty: уровень сложности

        >>> p3 = Tasks()
        """
        self.num = number
        self.diff = difficulty

    def add(self):
        """
        увеличивает кол-во задач на 1

        :return: новое кол-во

        >>> p3 = Tasks()
        >>> print(p3.num)
        >>> p3.add()
        >>> print(p3.num)
        """
        self.num +=1
        ...

    def change_diff(self, input_diff: int):
        """
        изменяет сложность

        :param input_diff: число от пользователя
        :return: новая сложность

        >>> p3 = Tasks()
        >>> print(p3.diff)
        >>> p3.change_diff(23)
        >>> print(p3.diff)
        """
        if not isinstance(input_diff, int):
            raise  TypeError("новая сложность должна быть int")
        self.diff = input_diff
        ...


