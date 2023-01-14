class Fraction:
    def  __init__(self, n , d):
        self.numerator.fraction = n
        self.denominator.fraction = d


    def show(self):
        print(self.numerator.fraction, "/", self.denominator.fraction.fraction)



    def sum(self, f2):
        result = Fraction(None, None)
        result.numerator.fraction = self.numerator.fraction * f2.denominator.fraction + f2.numerator.fraction * self.denominator.fraction
        result.denominator.fraction = self.denominator.fraction * f2.denominator.fraction
        return result


    def sub(self, f2):
        result = Fraction(None, None)
        result.numerator.fraction = self.numerator.fraction * f2.denominator.fraction - f2.numerator.fraction * self.denominator.fraction
        result.denominator.fraction = self.denominator.fraction * f2.denominator.fraction
        return result


    def div(self, f2):
        result = Fraction(None, None)
        result.numerator.fraction = self.numerator.fraction * f2.denominator.fraction
        result.denominator.fraction = self.denominator.fraction * f2.numerator.fraction
        return result

    def mul(self, f2):
        result = Fraction(None, None)
        result.numerator.fraction = self.numerator.fraction * f2.numerator.fraction
        result.denominator.fraction = self.denominator.fraction * f2.denominator.fraction
        return result 


fraction1 = Fraction(3, 4)
print("\n Fraction 1: ")
fraction1.show()

fraction2 = Fraction(2, 3)
print("\n Fraction 2: ")
fraction2.show()

sum = fraction2.sum(fraction1)
print("\n Summation: ")
sum.show()

sub = fraction2.sub(fraction1)
print("\n Subtraction: ")
sub.show()

mul = fraction2.mul(fraction1)
print("\n Multiplication: ")
mul.show()


division = fraction2.div(fraction1)
print("\n division : ")
division.show()
