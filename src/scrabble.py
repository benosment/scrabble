#! /usr/bin/env python
#
# Ben Osment
# Mon Nov 11 06:37:22 2013

"""Scrabble - given a set of letters, return the highest scoring word"""

import argparse
import logging

def parse_args():
    # build the command line parser, setup the logger
    parser = argparse.ArgumentParser(description='given a set of letters, return the highest scoring word')
    parser.add_argument('letters',
                        action='store',
                        nargs='+',
                        help='letters to construct word out of')
    parser.add_argument('--debug', action='store_true',
                        help='display debug information')
    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(name)s[%(funcName)s] %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s')
    return args


def main():
    args = parse_args()


if __name__ == '__main__':
    main()

