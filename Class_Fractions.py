import fractions
from sklearn.metrics import f1_score


class Fractions:
    def __init__(self,n1,d1,n2,d2):
        self.numerator_1 = n1
        self.denominator_1 = d1
        #----------------------#
        self.numerator_2 = n2
        self.denominator_2 = d2

    def add(self):
        F1 = (self.numerator_1 * self.denominator_2) / (self.denominator_1 * self.denominator_2)
        F2 = (self.numerator_2 * self.denominator_1) / (self.denominator_2 * self.denominator_1)
        aw = (F1 + F2)
        print(aw)

    def sub(self):
        F1 = (self.numerator_1 * self.denominator_2) / (self.denominator_1 * self.denominator_2)
        F2 = (self.numerator_2 * self.denominator_1) / (self.denominator_1 * self.denominator_1)
        aw = (F1 - F2)
        print(aw)
    
    def mul(self):
        aw= (self.numerator_1 * self.numerator_2)
        aw2= (self.denominator_1 * self.denominator_2)
        print(aw,"/",aw2)

    def div(self):
        aw= (self.numerator_1 * self.denominator_2)
        aw2= (self.numerator_2 * self.denominator_1)
        print(aw,"/",aw2)

    def show(self):
        pass

sample = Fractions(1,3,2,5)
sample.add()
sample.sub()
sample.mul()
sample.div()