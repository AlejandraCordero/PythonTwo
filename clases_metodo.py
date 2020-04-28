print("Hello World")
print("Hello World")
class CarToyota:
    marca = "toyota"
    instance_count=0
    
    @classmethod
    def increment_instance_count(cls):
        CarToyota.instance_count +=1
        
    def __init__(self,color,modelo):
        self.color=color
        self.modelo=modelo
        
    def encender(self):
        print("Coche encendido")
        
    def avanzar(self):
        print("Coche avanzando")
    
    def cambia_color(self,color):
        self.color=color
        
class Authentication:
    @classmethod
    def register(cls,username,password):
        print("Usuario registrado")
    @classmethod
    def login(cls,username,password):
        print("Welcome")

carro1=CarToyota("x","y")

carro2=CarToyota("x2","y2")

CarToyota.increment_instance_count()
print(CarToyota.instance_count)

Authentication.register("ale123","123")