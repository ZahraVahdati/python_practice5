class Date:
    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y , "/" , self.m , "/" , self.d)


    def add(self,Date_2):
        result=Date(None, None, None)
        result.y= self.y + Date_2.y
        result.m = self.m +Date_2.m
        result.d = self.d + Date_2.d

        if result.d >= 30:
            result.d -= 30
            result.m += 1

        if result.m >= 12:
            result.m -= 12
            result.y += 1

        return result


        def sub(self,Date_2):
          result=Date(None, None, None)
          result.y= self.y - Date_2.y
          result.m = self.m - Date_2.m
          result.d = self.d - Date_2.d

        if result.d <0 :
            result.d += 30
            result.m -= 1

        if result.m < 12:
            result.m += 12
            result.y -= 1

        return result


Date_1 = Date(1381, 10, 22)
Date_2 = Date(1401, 10, 15)


print("Date_1: ")
Date_1.show()

print("Date_2: ")
Date_2.show()

a= Date_1.add(Date_2)
print("add: ")
a.show()

s= Date_1.sub(Date_2)
print("sub: ")
s.show()

