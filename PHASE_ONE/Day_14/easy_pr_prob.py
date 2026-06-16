# In this we will solve some easy level practice problems

#Q1. Create a Car class with:

#Attributes: brand, model, year, speed
#Method accelerate(amount) → increases speed
#Method brake(amount) → decreases speed (not below 0)
#Method get_info() → prints all details

class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount  # updates THIS car's speed
        return self.speed

    def brake(self, amount):
        if decreased_speed < 0:
            final_speed =  0
            return final_speed
        else:
            return decreased_speed
            
        
    def get_info(self):

        car1 = Car("Toyota","Grande",2016,120)
        car1.accelerate(20)
        car1.brake(50)

        print(car1)

    


    result = get_info()                
    print(result)