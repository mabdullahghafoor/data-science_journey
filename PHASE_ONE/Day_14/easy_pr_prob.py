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

    def accelerate(self, amount):
        self.speed += amount  # updates THIS car's speed
        return self.speed

    def brake(self, amount):
        self.speed -= amount  # reduce speed

        if self.speed < 0:
            self.speed = 0

        return self.speed

    def get_info(self):
        print("Car Info:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Speed:", self.speed)


# Creating object
car1 = Car("Toyota", "Grande", 2016, 120)

car1.accelerate(20)
car1.brake(50)

car1.get_info()