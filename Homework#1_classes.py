print("María Alejandra Mamani Cordero")
print("Homework 1")

print("---Abstraction 1")
class book:
    def __init__(self, title, typee, year, publisher,quantity):
        self.title= title
        self.typee = typee
        self.year=year
        self.publisher=publisher
        self.quantity=quantity
        
        
    def copyy(self):
        print("Copy of : ", self.title)
        self.quantity += 1
        print("Quantity : ", self.quantity)
        
    def lend(self):
        print("Lend of : ", self.title)
        self.quantity -= 1
        print("Quantity : ", self.quantity)
        
    def find_book(self,search_book):
        print("Find the book: ")
        if search_book == self.title:
            print("It's here: ",self.title)
        else:
            print("The book was sold")
        
    def __str__(self):
        return "Book: {} , {} , {} , {} , {}".format(self.title, self.typee,self.year,self.publisher,self.quantity)

print("Book")
b=book("Bridge","Romantic",2010,"San Lorenzo",5)
print(b)
b.copyy()
print(b)
b.lend()
print(b)
b.find_book("The rat")
print(b)

print(" ")
print("---Abstraction 2")

class printer:
    def __init__(self, owner, typee, cost, color):
        self.owner=owner
        self.typee = typee
        self.cost=cost
        self.color=color
    
    def turn_on(self):
        print("Inpresora encendida")
    
    def turn_off(self):
        print("Impresora apagada")
    
    def printt(self, tipo):
        if self.typee==tipo:
            print("Imprimiendo")
        else:
            print("Impresora apagada")
    
    def sell(self, tipo, cost):
        if self.typee==tipo:
            if self.cost==cost:
                print("La impresora es: ",self.typee)
        
            else:
                print("No encontrado")
                
    def __str__(self):
        return "Printer: {} , {} , {} , {}".format(self.owner, self.typee,self.cost,self.color)


print("Printer")   
p=printer("Ale","Toshiba",125,"pink")
print(p)
p.turn_on()
print(p)
p.turn_off()
print(p)
p.sell("Toshiba",12)
print(p)
        