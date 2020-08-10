import math
from queue import PriorityQueue
from super_taxi.model.generics import Coordinate
from super_taxi.model.taxis import Taxi


def manhattan_distance(coordinate1:Coordinate, coordinate2:Coordinate):
    return abs(coordinate1.x - coordinate2.x) + abs(coordinate1.y - coordinate2.y)


def nearest_taxi(taxi_queue: PriorityQueue, location, distance_fun=manhattan_distance) -> Taxi:
    selected_taxi = None
    min_dist = math.inf
    while taxi_queue.queue:
        taxi = taxi_queue.get()[1]
        dist = distance_fun(taxi.position, location)
        if dist < min_dist:
            min_dist = dist
            selected_taxi = taxi
            selected_taxi.pickup_distance = dist
    return selected_taxi

