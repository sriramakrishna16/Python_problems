class vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def start(self):
        print(self.name , "engine started")

    def show_details(self):
        print("brand ", self.name)
        print("speed ", self.speed)

class car(vehicle):
    def __init__(self, name, speed, fueltype):
        super().__init__(name, speed)
        self.fueltype = fueltype
    def start(self):
        print(self.fueltype, "engine started")
    def drive(self):
        print(self.name, "car is driving")

    def show_details(self):
            print("Name :", self.name)
            print("Speed :", self.speed)
            print("Type :", self.fueltype)

class bike(vehicle):
    def __init__(self, name, speed, type):
        super().__init__(name, speed)
        self.type = type

    def start(self):
        if (self.type).lower() == "petrol":
            print(self.type, "engine started")
        else:
            print(self.type, "started")

    def drive(self):
        print(self.name, "started driving")

    def show_details(self):
        print("Name :", self.name)
        print("Speed :", self.speed)
        print("Type :", self.type)


def do(obj):
    obj.start()
    obj.drive()
    obj.show_details()


bike1 = bike("Yamaha", 120, "petrol")
do(bike1)

car1 = car("Toyoto", 180, "Diesel")
do(car1)