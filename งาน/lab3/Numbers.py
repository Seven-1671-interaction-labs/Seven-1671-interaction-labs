class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls, Numbers):
        if Numbers % 2 == 0:
            factor1 = Numbers // 2
            factor2 = Numbers // 2
        else:
            factor1 = Numbers // 2
            factor2 = Numbers // 2 + 1
        return f"factors of {Numbers} is {factor1} and {factor2}"

    @staticmethod
    def is_valid_divisor(Numbers):
        if Numbers != 0:
            return f"{Numbers} is a valid divisor"
        else:
            return f"{Numbers} is not a valid divisor"


if __name__ == '__main__':
    print(f'2+3 is {Numbers(2, 3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))