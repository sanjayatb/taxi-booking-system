#!/usr/bin/env python3

import argparse
from super_taxi.taxi_system import taxi_system
from super_taxi.model.taxis import Taxi,TaxiSuvCar,TaxiCar
from super_taxi.api.booking_api import app


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main(args=None):
    if not args:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("--clock", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="Activate System clock")
        args = arg_parser.parse_args()
        # arg_parser.print_help()
        taxis = [TaxiCar(1), TaxiSuvCar(2), TaxiCar(3), Taxi(4), Taxi()]
        taxi_system.register(taxis)
        taxi_system.opt_in_for_rides(taxi_ids=[1, 2, 3])
        taxi_system.run(run_clock=args.clock)
        app.run(port=8080)
    else:
        exit(1)


if __name__ == "__main__":
    main()
