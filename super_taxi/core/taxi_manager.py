"""
Taxi register will be the database facing pojo, all registered taxis will be there
"""
from super_taxi.model.taxis import Taxi


class TaxiRegister():
    def __init__(self):
        self.__registry = []

    def register(self, taxi: Taxi):
        taxi.id = taxi.id if taxi.id else self.__get_taxi_id()
        self.__registry.append(taxi)
        return taxi

    def unregister(self, taxi: Taxi):
        self.__registry.remove(taxi)

    def __get_taxi_id(self):
        return len(self.__registry) + 1

    def registered_taxi_count(self):
        return len(self.__registry)

    def get_all_registered_taxis(self):
        return self.__registry

    def reset(self):
        self.__registry.clear()

# maintain active vehicles
# Selected vehicles for rides, this will contain all active vehicles


class TaxiManager:
    def __init__(self):
        self.__active_taxis = []

    def opt_in(self,taxi):
        self.__active_taxis.append(taxi)

    def opt_out(self,taxi):
        self.__active_taxis.remove(taxi)

    def get_active_taxis(self):
        return self.__active_taxis

    def reset(self):
        self.__active_taxis.clear()


##tsingleton classes
taxi_register = TaxiRegister()
taxi_manager = TaxiManager()

