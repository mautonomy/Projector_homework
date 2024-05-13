# task 1

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def add(self, another_country):
        self.name += ' ' + another_country.name
        self.population += another_country.population

        return self 
    

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)

print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)


# task 2

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def __add__(self, another_country):
        new_name = self.name + ' ' + another_country.name
        new_population = self.population + another_country.population
        return Country(new_name, new_population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.name)
print(bosnia_herzegovina.population)


# Task 3

class Car:
    def __init__(self, brand, model, year, speed=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        self.speed += 5
        
    def brake(self):
        self.speed -= 5
        
    def display_speed(self):
        print(f"Speed of {self.brand} {self.model} {self.year} is {self.speed} km/h.")

car1 = Car("Toyota", "Prado", 2023)
car1.accelerate()
car1.display_speed()
        
        
            