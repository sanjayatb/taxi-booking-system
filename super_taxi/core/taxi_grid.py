from super_taxi.model.grid import Grid
from super_taxi.model.taxis import Taxi


class TaxiGrid(Grid):
    def __init__(self):
        Grid.__init__(self)
        self.taxis = []

    def add_taxis(self,taxis:Taxi):
        if isinstance(taxis,Taxi):
            self.taxis.append(taxis)
        else:
            self.taxis.extend(taxis)

    def time_tick(self,time_unit):
        print(f"Taxi Grid : {time_unit} time unit")
        self.__update_position()
        self.__print_state()

    def __update_position(self):
        for taxi in self.taxis:
            if taxi.ride is None:
                continue
            current = taxi.position
            destination = taxi.ride.destination if taxi.ride.on_trip else taxi.ride.source
            # print(f"id : {taxi.id} before : {current} : {destination}")
            self.__move(taxi, destination.x - current.x, destination.y - current.y)
            # print(f"id : {taxi.id} after  : {current} : {destination}")
            if current.x == taxi.ride.source.x and current.y == taxi.ride.source.y:  ## Taxi reach pickup
                print(f"\ttaxi : {taxi.id} reached pickup : {current}")
                taxi.ride.on_trip = True

            if current.x == taxi.ride.destination.x and current.y == taxi.ride.destination.y:  ## Taxi reach destination
                print(f"\ttaxi : {taxi.id} reached destination : {current}")

    def __move(self,taxi,x_dir,y_dir):
        if x_dir > 0:
            taxi.position.x += 1
        elif y_dir > 0:
            taxi.position.y += 1
        elif x_dir < 0:
            taxi.position.x -= 1
        elif y_dir < 0:
            taxi.position.y -= 1

    def __print_state(self ):
        for taxi in self.taxis:
            print(f"\ttaxi id: {taxi.id}, position:{taxi.position}")


grid = TaxiGrid()