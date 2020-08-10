import unittest
from super_taxi.model.generics import Coordinate
from super_taxi.core.functions import manhattan_distance,nearest_taxi
from super_taxi.model.taxis import TaxiCar
from queue import PriorityQueue


class FunctionsTestCases(unittest.TestCase):
    def test_manhattan_distance(self):
        cor1 = Coordinate(1,1)
        cor2 = Coordinate(5,5)
        self.assertEqual(8, manhattan_distance(cor1,cor2))

    def test_nearest_vehicle(self):
        location = Coordinate(1,2)
        queue = PriorityQueue()
        car1 = TaxiCar(1)
        car2 = TaxiCar(2)
        queue.put((car1.id,car1))
        queue.put((car2.id,car2))
        self.assertEqual(car1, nearest_taxi(queue,location))


if __name__ == '__main__':
    unittest.main()
