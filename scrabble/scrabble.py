#! /usr/bin/env python
#
# Ben Osment
# Mon Nov 11 06:37:22 2013

"""Scrabble - given a set of letters, return the highest scoring word"""

import argparse
import logging

scores = {"a": 1,
          "b": 3,
          "c": 3,
          "d": 2,
          "e": 1,
          "f": 4,
          "g": 2,
          "h": 4,
          "i": 1,
          "j": 8,
          "k": 5,
          "l": 1,
          "m": 3,
          "n": 1,
          "o": 1,
          "p": 3,
          "q": 10,
          "r": 1,
          "s": 1,
          "t": 1,
          "u": 1,
          "v": 4,
          "w": 4,
          "x": 8,
          "y": 4,
          "z": 10}


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
    # lowercase all letters
    args.letters = args.letters[0].lower()
    return args


def build_wordlist(filename):
    ''' reads in a file which contains one word on a line, returns
        a list of all of the words'''
    with open(filename) as f:
        words = [line.strip().lower() for line in f.readlines()]
    return words


def find_highest(letters, wordlist):
    # form a list of tuples which are creatable
    creatable_words = get_creatable_words(letters, wordlist)
    highest_word = None
    highest_score = None
    for word_score in creatable_words:
        w, s = word_score
        if s > highest_score:
            highest_score = s
            highest_word = w
    return highest_word


def all_scores(letters, wordlist):
    # form a list of tuples which are creatable
    creatable_words = get_creatable_words(letters, wordlist)
    creatable_words.sort(key=lambda t: t[1], reverse=True)
    return creatable_words


def get_creatable_words(letters, wordlist):
    return [(word, get_word_score(word))
            for word in wordlist if creatable(word, letters)]


def get_word_score(word):
    ''' Returns a cumulative score for Scrabble words '''
    return sum([scores[letter] for letter in word])


def print_all_scores(word_scores):
    for word_score in word_scores:
        word, score = word_score
        print score, word


def creatable(word, letters):
    ''' Returns True if a word can be constructed given the letters
        returns False otherwise'''
    letter_list = list(letters)
    for letter in word:
        if letter in letter_list:
            letter_list.remove(letter)
        else:
            return False
    return True


def main():
    # parse the args
    args = parse_args()
    # generate the list of acceptable words
    wordlist = build_wordlist(args.wordlist_filename)
    # find the highest words
    #find_highest(args.letters, wordlist)
    print_all_scores(all_scores(args.letters, wordlist))


if __name__ == '__main__':
    main()
