print("Hello World")
class Complejos:
    def __init__(self,imaginaria,real):
        self.imaginaria=imaginaria
        self.real=real
        
    def __str__(self):
        return "{}+{}i".format(self.real,self.imaginaria)
    
    def __add__(self,otro_complejo):  #+
        real=self.real+otro_complejo.real
        imaginaria=self.imaginaria+otro_complejo.imaginaria
        return Complejos(real=real,imaginaria=imaginaria)
        
    def __sub__(self,otro_complejo):  #+
        real=self.real-otro_complejo.real
        imaginaria=self.imaginaria-otro_complejo.imaginaria
        return Complejos(real=real,imaginaria=imaginaria)
        
    def __mul__(self,otro_complejo):  #+
        real=self.real*otro_complejo.real
        imaginaria=self.imaginaria*otro_complejo.imaginaria
        return Complejos(real=real,imaginaria=imaginaria) 

complejo1=Complejos(3,1)
complejo2=Complejos(3,1)
print('suma: ',complejo1+complejo2)
print('resta: ',complejo1-complejo2)

a=3
b=5
print(a+b)

