class Fraction:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        x = self.gcd2(a, b)
        self.a /= x
        self.b /= x
    
    def gcd2(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self, a, b):
        # 求最小公倍数
        x = self.gcd2(a, b)
        return (a/x) * b

    def __add__(self, other):
        # 1/12 + 1/20, 先通分，算出最小公倍数
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * (fenmu / b) + c * (fenmu / d)
        return Fraction(fenzi, fenmu)

    def __str__(self) -> str:
        return '%d/%d' % (self.a, self.b)
    
a = Fraction(1, 3)
b = Fraction(1, 2)
print(a+b)