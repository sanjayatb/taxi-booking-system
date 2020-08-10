import unittest
from super_taxi.core.ride_handler import RideHandler
from super_taxi.model.generics import Ride,Coordinate
from super_taxi.model.taxis import TaxiCar


class RideHandlerTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = []
        self.car1 = TaxiCar(1)
        self.car2 = TaxiCar(2)
        self.queue.append(self.car1)
        self.queue.append(self.car2)
        self.handler = RideHandler(taxis=self.queue)

    def test_get_nearest_taxi(self):
        ride1 = Ride(Coordinate(1, 0), Coordinate(1, 1))
        taxi = self.handler.get_nearest_taxi(ride1)
        self.assertEqual(self.car1,taxi)