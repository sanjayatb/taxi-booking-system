#!/usr/bin/env python3

import argparse


def main(args=None):
    if not args:
        arg_parser = argparse.ArgumentParser()
        args = arg_parser.parse_args()
        print(args)
    else:
        exit(1)


if __name__ == "__main__":
    main()
