"""
Responsible for mange rides
"""
from queue import PriorityQueue
from super_taxi.core.functions import manhattan_distance, nearest_taxi
from super_taxi.model.generics import Ride
from super_taxi.model.taxis import Taxi
from super_taxi.core.clock import TimerCallBack
from super_taxi.core.taxi_manager import taxi_manager


class RideHandler(TimerCallBack):
    def __init__(self, taxis=[]):
        self.__time_factor = 1  ## Distance to time factor
        self.__booked_taxis = []
        self.__available_taxis = taxis

    def get_nearest_taxi(self, ride: Ride) -> Taxi:
        queue = PriorityQueue()  # getting available taxi based of priority given
        for taxi in self.__available_taxis:
            queue.put((taxi.id, taxi))  # id base priority
        booked_taxi = nearest_taxi(queue, ride.source)
        self.__arrange_booking(booked_taxi, ride)
        return booked_taxi

    def __arrange_booking(self, taxi: Taxi, ride: Ride):
        if taxi is None:
            return

        taxi.booked_for(ride)
        trip_distance = manhattan_distance(ride.destination, ride.source)
        ride.set_trip_time(self.__time_factor * trip_distance)
        pickup_time = self.__time_factor * taxi.pickup_distance
        ride.set_total_time(ride.trip_time + pickup_time)
        # taxi.position = ride.destination  ## final position of taxi
        self.__booked_taxis.append(taxi)
        self.__available_taxis.remove(taxi)

    def get_lowest_fair_taxi(self, ride):
        pass

    def get_booked_taxis(self):
        return self.__booked_taxis

    def time_tick(self, time_unit=0):
        self.__update_time()
        self.__print_state()

    def __update_time(self):
        for vehicle in self.__booked_taxis:
            if vehicle.ride.remaining_time > 0:
                vehicle.ride.remaining_time -= 1
            elif vehicle.ride.remaining_time == 0:
                vehicle.ride = None
                vehicle.booked = False
                self.__available_taxis.append(vehicle)
                self.__booked_taxis.remove(vehicle)

    def reset(self):
        self.__booked_taxis.clear()
        self.__available_taxis.clear()
        self.__available_taxis.extend(taxi_manager.get_active_taxis())

    def __print_state(self):
        print("Available taxis count : ",
              len(self.__available_taxis) if len(self.__available_taxis) != 0 else "No taxis")
        for taxi in self.__available_taxis:
            print(f"\ttaxi id : {taxi.id}, position : {taxi.position}")

        print("Booked taxis count : ", len(self.__booked_taxis) if len(self.__booked_taxis) != 0 else "No taxis")
        for taxi in self.__booked_taxis:
            print(
                f"\ttaxi id : {taxi.id}, from: {taxi.ride.source}, to: {taxi.ride.destination},time_remain : {taxi.ride.remaining_time}")
