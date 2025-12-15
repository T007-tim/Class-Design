
# Vehicle base class
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def vehicle_info(self):
        print(f"Brand: {self.brand}, Max Speed: {self.max_speed} km/h")

    def move(self):
        print("The vehicle is moving")


# Child class 1
class Car(Vehicle):
    def move(self):
        print("The car is driving ")


# Child class 2
class Bike(Vehicle):
    def move(self):
        print("The bike is riding")


# Child class 3
class Truck(Vehicle):
    def move(self):
        print("The truck is transporting goods")


# Smartphone base class
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def use(self):
        print("Using the smartphone")


# Child class
class AndroidPhone(Smartphone):
    def use(self):
        print(f"Using {self.brand} {self.model} to run Android apps 📱")


class IPhone(Smartphone):
    def use(self):
        print(f"Using {self.brand} {self.model} with iOS 🍎")


# Demonstration of polymorphism
def demonstrate_polymorphism(objects):
    for obj in objects:
        obj.move() if isinstance(obj, Vehicle) else obj.use()


# Main program
if __name__ == "__main__":
    # Vehicle objects
    car = Car("Toyota", 180)
    bike = Bike("Yamaha", 120)
    truck = Truck("Isuzu", 100)

    vehicles = [car, bike, truck]

    print("Vehicle Polymorphism Demo:")
    for vehicle in vehicles:
        vehicle.vehicle_info()
        vehicle.move()
        print()

    # Smartphone objects
    phone1 = AndroidPhone("Samsung", "Galaxy S23")
    phone2 = IPhone("Apple", "iPhone 14")

    phones = [phone1, phone2]

    print("Smartphone Polymorphism Demo:")
    for phone in phones:
        phone.use()








