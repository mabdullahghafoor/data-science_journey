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
        increase_speed += increase_speed
        return increase_speed

    def brake(amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        
    def get_info():

        car_brand = Car.brand
        car_model = Car.model
        car_year = Car.year
        car_speed = Car.speed

        pos_speed = Car.accelerate(120)
        neg_speed = Car.brake(20)

        car_brand = "Toyota"
        car_model = "Altis"
        car_year = 2010
        car_speed = 110

