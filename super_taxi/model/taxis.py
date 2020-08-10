from super_taxi.model.generics import Vehicle, Coordinate
from super_taxi.model.cars import Car,SUVCar


class Taxi(Vehicle):
    def __init__(self, id=None):
        Vehicle.__init__(self, id=id)
        self.position = Coordinate(0, 0)
        self.ride = None
        self.booked = False
        self.pickup_distance = 0

    def booked_for(self, ride):
        self.ride = ride
        self.booked = True

    def is_booked(self):
        return self.booked

    def reset(self):
        self.position = Coordinate(0, 0)
        self.ride = None
        self.booked = False
        self.pickup_distance = 0


class TaxiCar(Car, Taxi):
    def __init__(self, id=None):
        Car.__init__(self, id)
        Taxi.__init__(self, id)


class TaxiSuvCar(SUVCar, Taxi):
    def __init__(self, id=None):
        SUVCar.__init__(self, id)
        Taxi.__init__(self, id)
