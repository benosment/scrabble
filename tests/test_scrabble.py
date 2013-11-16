#! /usr/bin/env python
#
# Ben Osment
# Mon Nov 11 06:39:55 2013

"""Unit tests for scrabble.py"""

import unittest
import sys
import os

current_dir = os.getcwd()
src_dir = os.path.join(current_dir, 'scrabble')
tests_dir = os.path.join(current_dir, 'tests')

# add the source directory to the load path
sys.path.append(src_dir)

import scrabble


class TestScrabble(unittest.TestCase):

    def setUp(self):
        self.words = scrabble.build_wordlist(os.path.join(tests_dir,
                                                          'test_wordlist.txt'))
        self.letters = 'DOGCAT'

    def test_wordlist(self):
        correct_words = ['dog', 'cat', 'rabbit']
        self.assertEquals(self.words, correct_words)

    def test_highest(self):
        # self.assertEquals(scrabble.find_highest(self.letters,
        #                                         self.words), 'DOG')
        pass

    def test_wordscore(self):
        self.assertEquals(scrabble.get_word_score('faze'), 16)
        self.assertEquals(scrabble.get_word_score('fiz'), 15)
        self.assertEquals(scrabble.get_word_score('ben'), 5)

    def test_creatable(self):
        self.assertTrue(scrabble.creatable('hat', 'aahhtt'))
        self.assertFalse(scrabble.creatable('noon', 'nott'))


if __name__ == '__main__':

    unittest.main()
