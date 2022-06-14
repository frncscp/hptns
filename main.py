class Ptgrs:
    def __init__(self, h, c1, c2): #hipotenusa, catetos
        self.h, self.c1, self.c2 = h, c1, c2
    def check(self): #saber si se cumple el teorema de pitágoras
        return self.h%((self.c1**2)+(self.c2**2))**0.5 < 0.05
    def pitagorazo(self, lado): #aplicar teorema por despeje
        if lado == 'h':
            self.h = ((mpf(self.c1**2)) + mpf(self.c2**2))**.5
            return self.h
        elif lado == 'c1':
            self.c1 = ((mpf(self.h**2)) - mpf(self.c2**2))**.5
            return self.c1
        elif lado == 'c2':
            self.c2 = ((mpf(self.h**2)) - mpf(self.c1**2))**.5
            return self.c2 
