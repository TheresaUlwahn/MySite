a = 1
b = 'hej'

print(a)
print(b)

def add(x, y):
    return x + y

print(add(4, 5))

class Car():
    TIRES = 4
    DOORS = 4

    def manufactored_in(self):
        return 'Not defined'

class Audi(Car):
    def manufactored_in(self):
        return 'Germany'

class Tesla(Car):
    DOORS = 5

    # def manufactored_in(self):
    #     return 'USA'

tesla = Tesla()

print(tesla.manufactored_in())
        