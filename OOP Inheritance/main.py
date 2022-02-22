class Calc:
    """Калькулятор для прибавления цифры 3"""
    def add_numb(self, x):
        a = x + 3
        return a

class Sum_multiply(Calc):
    """Калькулятор для прибавления цифры 3 и умнажение на цифру 5"""
    def multiply_numb(self, x):
        a = x * 5
        return a
c = Calc()
s = Sum_multiply()
print (s.add_numb(2))
print (s.multiply_numb(2))
