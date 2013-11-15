#! /usr/bin/env python
#
# Ben Osment
# Mon Nov 11 06:37:22 2013

"""Scrabble - given a set of letters, return the highest scoring word"""

import argparse
import logging


def parse_args():
    # build the command line parser, setup the logger
    parser = argparse.ArgumentParser(description='given a set of letters,'
                                     'return the highest scoring word')
    parser.add_argument('letters',
                        action='store',
                        nargs='+',
                        help='letters to construct word out of')
    parser.add_argument('-w',
                        '--wordlist_filename',
                        help='wordlist to use',
                        action='store',
                        default='../resources/sowpods-wordlist.txt')
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


def build_wordlist(filename):
    ''' reads in a file which contains one word on a line, returns
        a list of all of the words'''
    with open(filename) as f:
        words = [line.strip() for line in f.readlines()]
    return words


def find_highest(filename):
    pass


def main():
    # parse the args
    args = parse_args()
    # generate the list of acceptable words
    wordlist = build_wordlist(args.wordlist_filename)
    # find the highest words
    find_highest(args.letters, wordlist)


if __name__ == '__main__':
    main()
