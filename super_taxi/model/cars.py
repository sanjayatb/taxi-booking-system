from super_taxi.model.generics import Vehicle,VehicleType


class Car(Vehicle):
    def __init__(self,id=None):
        Vehicle.__init__(self,id=id,type=VehicleType.Car)


class SedanCar(Car):
    def __init__(self,id=None):
        Car.__init__(self,id)


class SUVCar(Car):
    def __init__(self,id=None):
        Car.__init__(self,id)