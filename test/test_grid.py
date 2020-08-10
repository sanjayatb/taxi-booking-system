import unittest
from super_taxi.model.generics import Ride,Coordinate
from super_taxi.core.taxi_grid import grid
from super_taxi.model.taxis import TaxiCar


class GridTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = []
        self.car1 = TaxiCar(1)
        self.car2 = TaxiCar(2)
        ride1 = Ride(Coordinate(1,0),Coordinate(1,1))
        ride2 = Ride(Coordinate(1,1),Coordinate(5,5))
        self.car1.ride = ride1
        self.car2.ride = ride2
        self.queue.append(self.car1)
        self.queue.append(self.car2)

    def test_add_taxis(self):
        grid.add_taxis(self.queue)
        self.assertEqual(2, len(grid.taxis))

    def test_time_tick(self):
        grid.add_taxis(self.queue)
        grid.time_tick(1)
        grid.time_tick(2)
        self.assertEqual(1,self.car1.position.x)
        self.assertEqual(1,self.car1.position.y)
        grid.time_tick(3)


if __name__ == '__main__':
    unittest.main()
