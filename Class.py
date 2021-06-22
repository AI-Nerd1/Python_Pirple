import random
class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.Needs_maintenance = False
        self.Trips_since_maintenance = 0

    def getMaintenance_status(self):
        return self.Needs_maintenance

    def getTrips_since_maintenance(self):
        return self.Trips_since_maintenance

    def trip_started(self):
        self.Trips_since_maintenance += 1
        if self.Trips_since_maintenance >= 100:
            self.Needs_maintenance = True

    def repair(self):
        if self.Needs_maintenance:
            self.Trips_since_maintenance = 0
            self.Needs_maintenance = False
            return True
        else:
            return False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False

    def Drive(self):
        if not self.isDriving:
            self.isDriving = True
            return True
        else:
            return False

    def Stop(self):
        if self.isDriving:
            self.isDriving = False
            self.trip_started()
            return True
        else:
            return False

    def __str__(self):
        return "Car Name: " + self.make + "\nCar Model:" + self.model + " \nYear: " + str(self.year) + " \nweight: " + str(
            self.weight) + "\nNumber of times driven: " + str(
            self.Trips_since_maintenance) + " times \nStatus: " + (
                   "Needs " if self.Needs_maintenance else " Doesn't need ") + "maintenance.\n"


Car1 = Cars("Mercedes", "4-matic", 2021, "4573 lbs")
Car2 = Cars("Audi", "De-ron", 2018, "3963 lbs")
Car3 = Cars("Toyota", "Hilander", 2019, "5273 lbs")


for i in range(random.randrange(200)):
    Car1.Drive()
    Car1.Stop()

for i in range(random.randrange(200)):
    Car2.Drive()
    Car2.Stop()

for i in range(random.randrange(200)):
    Car3.Drive()
    Car3.Stop()


print(Car1)
print(Car2)
print(Car3)




class Plane(Vehicle):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False

    def Fly(self):
        if not self.getMaintenance_status():
            if not self.isFlying:
                self.isFlying = True
                return True
            else:
                return False
        # else:
        #     print("Plane needs to be repaired before flying again.")

    def Land(self):
        if self.isFlying:
            self.isFlying = False
            self.trip_started()
            return True
        else:
            return False

    def __str__(self):
        return "The plane is " + self.make + " " + self.model + " from year " + str(self.year) + " and weights " + str(
            self.weight) + "\nCurrently has been driven " + str(
            self.Trips_since_maintenance) + " times and " + (
                   "needs " if self.Needs_maintenance else " doesn't need ") + "maintenance.\n"

newPlane1 = Plane("Boeing", "777-200LR", 2018, 223168)

for i in range(random.randrange(300)):
    newPlane1.Fly()
    newPlane1.Land()

print(newPlane1)