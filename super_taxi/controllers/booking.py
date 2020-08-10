from super_taxi.model.generics import Request, Response, Ride, Coordinate
from super_taxi.core.ride_handler import RideHandler


class BookingController:
    def __init__(self):
        self.handler = None

    def assign_handler(self,handler:RideHandler):
        self.handler = handler

    def create_booking(self, request: Request) -> Response:
        if self.handler is None:
            raise Exception('No handler found')

        source = Coordinate(request['source']['x'], request['source']['y'])
        destination = Coordinate(request['destination']['x'], request['destination']['y'])

        ride = Ride(source, destination)
        taxi = self.handler.get_nearest_taxi(ride)

        response = Response()
        if taxi is None:
            return response

        response.car_id = taxi.id
        response.total_time = taxi.ride.total_time
        return response

    def tick(self):
        self.handler.time_tick()

    def reset(self):
        self.handler.reset()

#Singleton booking controler
book_controller = BookingController()