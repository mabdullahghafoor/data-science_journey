# In this we will solve some easy level practice problems

#Q1. Create a Car class with:

#Attributes: brand, model, year, speed
#Method accelerate(amount) → increases speed
#Method brake(amount) → decreases speed (not below 0)
#Method get_info() → prints all details


class Car:

    def __init__(self, brand, model,year,speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    


    def accelerate(self,amount):
        self.speed += amount
        return self.speed
    

    def brake(self, amount):
        
        self.speed -= amount

        if self.speed < 0:
            self.speed = 0

        return self.speed
    

    def get_info(self):

        print("Car Details")
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        print(f"Car Speed: {self.speed}")

# Creating Car Instance (Object)

car1 = Car("Toyota","GLI",2016,120)

car1.accelerate(20)
car1.brake(60)

car1.get_info()


#Q2. Without running, what prints?

class Animal:
    sound = "..."
    def speak(self):
        print(f"I say {self.sound}")

class Dog(Animal):
    sound = "Woof!"

class Cat(Animal):
    sound = "Meow!"

d = Dog()
c = Cat()
d.speak() # I say Woof
c.speak() # I say Meow
