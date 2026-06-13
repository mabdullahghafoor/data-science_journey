# In this we will solve some easy level practice problems

#Q1. Create a Car class with:

#Attributes: brand, model, year, speed
#Method accelerate(amount) → increases speed
#Method brake(amount) → decreases speed (not below 0)
#Method get_info() → prints all details

class Car:

    increase_speed = 0
    decrease_speed = 0
    def __init__(self,brand,model,year,speed):

        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed


    def accelerate(amount):
