class Parallelepiped:
    # Определение объекта класса с инициализацией
    def __init__ (self, R1=0, lenA=0, lenB=0, lenC=0):
        self.r = float(R1)
        self.a = float(lenA)
        self.b = float(lenB)
        self.c = float(lenC)

    def check (self):
        flag = False
        if ((self.a)**2+(self.b)**2+(self.c)**2)**(1/2)<=2*self.r:
            flag = True
        return flag

    def ostatok (self):
        import math
        v = 0
        v = ((4/3)*math.pi*(self.r**3))-(self.a*self.b*self.c)
        return v     
  
