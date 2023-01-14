
class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


    def show(self):
        print(self.h, ":", self.m, ":", self.s)


    def sum(self, t2):
        result = Time(None, None, None)
        result.h = self.h + t2.h
        result.m = self.m + t2.m
        result.s = self.s + t2.s

        if result.s >= 60:
            result.s -= 60
            result.m += 1

        if result.m >= 60:
            result.m -= 60
            result.h += 1

        return result


    def minus(self, t2):
        result = Time(None, None, None)
        result.h = self.h - t2.h
        result.m = self.m - t2.m
        result.s = self.s - t2.s

        if result.s < 0:
            result.s += 60
            result.m -= 1

        if result.m < 60:
            result.m += 60
            result.h -= 1

        return result


    def TtoS(self):
        Change1 = 3600 * self.h + 60 * self.m + self.s
        return Change1


def StoT(self):
    hour = int(self/3600)
    minute = int((self-hour*3600)/60)
    second1 = int(self - hour*3600 - minute*60)
    return [hour, minute, second1]

time1 = Time(8, 9, 10)
time2 = Time(8, 15, 20)
sanie = 4528

print("Time1: ")
time1.show()

print("Time2: ")
time2.show()

s = time1.sum(time2)
print("time1 + Time2 : ")
s.show()

m = time1.minus(time2)
print("time1 - Time2 equal to: ")
m.show()

second = time1.TtoS()
print("time1 Change to second:\n" ,second)

time = StoT(sanie)
print ("second Change to Time:\n", time[0], ":", time[1], ":", time[2])
