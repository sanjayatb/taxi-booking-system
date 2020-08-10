from flask.json import JSONEncoder,JSONDecoder
from enum import Enum


class Request():
    def __init__(self,request):
        self.source = request["source"]
        self.destination = request["destination"]


class Response(JSONEncoder):
    def __init__(self):
        self.car_id = None
        self.total_time = None


class ResponseEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Response):
            return {'car_id': obj.car_id, 'total_time': obj.total_time}
        return JSONEncoder.default(self,obj)


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class VehicleType(Enum):
    Car = 1
    Bike = 2
    Bus = 3
    Lorry = 4


class Vehicle:
    def __init__(self,id=None,type:VehicleType=None):
        self.id = id
        self.type = type


class Ride:
    def __init__(self,source:Coordinate,destination:Coordinate):
        self.source = source
        self.destination = destination
        self.on_trip = False ## will true once after pickup
        self.trip_distance = 0
        self.total_time = 0
        self.remaining_time = 0
        self.trip_time = 0

    def set_trip_distance(self,dist):
        self.trip_distance = dist

    def set_trip_time(self,time):
        self.trip_time = time

    def set_total_time(self,time):
        self.total_time = time
        self.remaining_time = time

    def get_remaining_time(self):
        return self.remaining_time

    def reset(self):
        self.source = None
        self.destination = None


