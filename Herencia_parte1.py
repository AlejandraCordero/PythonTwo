class ConejoPadre:
    def __init__(self,edad,color,tipo,nombre,genero):
        self.edad=edad
        self.color=color
        self.tipo=tipo
        self.nombre=nombre
        self.genero=genero
        
    def saltar(self):
        pass
    def correr(self):
        pass
    def dormir(self):
        pass
    def __str__(self):
        return ""
        
class ConejoHijo(ConejoPadre):
    def __init__(self):
        pass
    

#creamos los objetos    
papa_conejo=ConejoPadre(2,'blanco','castilla','pipo','macho')
hijo=ConejoHijo()

#print(dir(hijo))
#print(id(hijo))
#help(hijo)
'''
import cv2
dir(cv2)  #código
help(cv2)  #programador
'''