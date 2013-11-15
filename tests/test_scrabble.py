#! /usr/bin/env python
#
# Ben Osment
# Mon Nov 11 06:39:55 2013

"""Unit tests for scrabble.py"""

import unittest
import sys
import os

# add the source directory to the load path
sys.path.append(os.path.join(os.getcwd(), 'scrabble'))

import scrabble


class TestScrabble(unittest.TestCase):
    
    def test_wordlist(self):
        correct_words = ['dog', 'cat', 'rabbit']
        words = scrabble.build_wordlist('test_wordlist.txt')
        self.assertEquals(words, correct_words)

    def test_highest(self):
        pass


if __name__ == '__main__':

    unittest.main()
