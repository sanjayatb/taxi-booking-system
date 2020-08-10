import unittest
from super_taxi.controllers.booking import book_controller
from super_taxi.model.generics import Request,Ride,Coordinate
from super_taxi.core.ride_handler import RideHandler
from super_taxi.model.taxis import TaxiCar

class BookingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = []
        self.car1 = TaxiCar(1)
        self.car2 = TaxiCar(2)
        self.queue.append(self.car1)
        self.queue.append(self.car2)

    def test_create_booking(self):
        input = { "source": {'x': 1, 'y': 0},  "destination": {'x': 1, 'y': 1}}
        request = Request(input)
        self.assertRaises(Exception,book_controller.create_booking,request)

        handler = RideHandler(self.queue)
        book_controller.assign_handler(handler)
        response = book_controller.create_booking(request)
        self.assertEqual(1,response.car_id)
        self.assertEqual(2,response.total_time)


if __name__ == '__main__':
    unittest.main()
