#c python...
#py py
#highton
# python+java --->kotlin

class D:
    def inst_method(self,x,y):
        # pertenece a la instancia de una clase= objeto
        pass
    
    @staticmethod
    def static_method(x,y):
        pass
    
    @classmethod
    def cls_method(cls,x,y):
        pass
    
d=D() #instaciar el objeto
d.inst_method(1,2)  #Metodo de instancia
#inst_method (d,1,2)

#llamado desde la clase
d.static_method(1,2)
#static_method(1,2)

#llamado desde la clase
D.static_method(1,2)
#static_method(1,2)

d.cls_method(1,2)
#cls_method(type(D),x,y)

D.cls_method(1,2)
#cls_method(D,x,y)
        