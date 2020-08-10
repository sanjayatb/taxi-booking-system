from super_taxi.core.taxi_manager import taxi_register,taxi_manager
from super_taxi.core.ride_handler import RideHandler
from super_taxi.controllers.booking import book_controller
from super_taxi.core.clock import Clock
from super_taxi.model.taxis import Taxi
from super_taxi.core.taxi_grid import grid


class TaxiSystem:
    def __init__(self):
        self.__clock = None
        self.__grid = grid
        self.__taxi_register = taxi_register
        self.__taxi_manager = taxi_manager
        self.__book_controller = book_controller
        self.__ride_handler = None

    def register(self,taxi_list:Taxi):
        for taxi in taxi_list:
            self.__taxi_register.register(taxi)
        print("Registered taxis : ",[taxi.id for taxi in taxi_list])

    def opt_in_for_rides(self,taxi_ids:Taxi):
        taxi_list = self.__taxi_register.get_all_registered_taxis()
        for taxi in taxi_list:
            if taxi.id in taxi_ids:
                self.__taxi_manager.opt_in(taxi)
                self.__grid.add_taxis(taxi)
        print("Opt In taxis : ", [taxi.id for taxi in self.__taxi_manager.get_active_taxis()])

    def run(self,run_clock=False):
        self.__ride_handler = RideHandler(taxi_manager.get_active_taxis())
        self.__clock = Clock([self.__ride_handler, self.__grid])
        self.__book_controller.assign_handler(self.__ride_handler)
        self.__book_controller.assign_clock(self.__clock)
        if run_clock:  # Default will run system clock
            self.__clock.start()

    def reset(self):
        self.__ride_handler = RideHandler(self.__taxi_manager.get_active_taxis())
        self.__clock.reset()


taxi_system = TaxiSystem()
