import datetime

class Time:
    def __init__(self, h1, m1, s1, h2, m2, s2):
        self.hour1 = h1
        self.minute1 = m1
        self.second1 = s1
        #------------------#
        self.hour2 = h2
        self.minute2 = m2
        self.second2 = s2
    
    def add(self):
        if(self.minute1 <= 60 and self.minute2 <= 60):
            if(self.second1 <= 60 and self.second2 <= 60):
                awh= (self.hour1 + self.hour2)
                awm= (self.minute1 + self.minute2)
                aws= (self.second1 + self.second2)
                if(awm > 60 or aws > 60):
                    awmr = 60
                    awsr = 60
                    print("Time: ",awh,":",awmr,":",awsr)
                else:
                    print("Time: ",awh,":",awm,":",aws)

    def sub(self):
        if(self.minute1 <= 60 and self.minute2 <= 60):
            if(self.second1 <= 60 and self.second2 <= 60):
                awh= (self.hour1 - self.hour2)
                awm= (self.minute1 - self.minute2)
                aws= (self.second1 - self.second2)
                if(awm < 0 or aws < 0):
                    awmr = 0
                    awsr = 0
                    print("Time: ",awh,":",awmr,":",awsr)
                else:
                    print("Time: ",awh,":",awm,":",aws)

    def mul(self):
        if(self.minute1 <= 60 and self.minute2 <= 60):
            if(self.second1 <= 60 and self.second2 <= 60):
                awh= (self.hour1 * self.hour2)
                awm= (self.minute1 * self.minute2)
                aws= (self.second1 * self.second2)
                if(awm > 60 or aws > 60):
                    awmr = 60
                    awsr = 60
                    print("Time: ",awh,":",awmr,":",awsr)
                else:
                    print("Time: ",awh,":",awm,":",aws)

    def div(self):
        if(self.minute1 <= 60 and self.minute2 <= 60):
            if(self.second1 <= 60 and self.second2 <= 60):
                awh= (self.hour1 / self.hour2)
                awm= (self.minute1 / self.minute2)
                aws= (self.second1 / self.second2)
                if(awm < 0 or aws < 0):
                    awmr = 0
                    awsr = 0
                    print("Time: ",awh,":",awmr,":",awsr)
                else:
                    print("Time: ",awh,":",awm,":",aws)
    
    def stm(self):
        awh1 = str(datetime.timedelta(seconds=self.second1))
        awh2 = str(datetime.timedelta(seconds=self.second2))
        print(awh1)
        print(awh2)
    
    def show(self):
        pass

sample = Time(12,30,20,1,40,50)
sample.add()
sample.sub()
sample.mul()
sample.div()
sample.stm()