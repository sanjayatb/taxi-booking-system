#!/usr/bin/env python3

import argparse
from super_taxi.taxi_system import taxi_system
from super_taxi.model.taxis import Taxi,TaxiSuvCar,TaxiCar
from super_taxi.api.booking_api import app


def main(args=None):
    if not args:
        arg_parser = argparse.ArgumentParser()
        args = arg_parser.parse_args()
        print(args)
        taxis = [TaxiCar(1), TaxiSuvCar(2), TaxiCar(3), Taxi(4), Taxi()]
        taxi_system.register(taxis)
        taxi_system.opt_in_for_rides(taxi_ids=[1, 2, 3])
        taxi_system.run()
        app.run(port=8080)
    else:
        exit(1)


if __name__ == "__main__":
    main()
