import unittest

# noinspection PyUnresolvedReferences
import test.context
from util.word import Word


class TestWord(unittest.TestCase):

    def test_word_with_1_bit(self):
        self.assertEqual(Word(1, 0, 1, 0, bit=1), 0b1010)

    def test_word_with_4_bit(self):
        self.assertEqual(Word(0x3, 0xf, 0xa, 0xe, bit=4), 0x3fae)

    def test_word_with_16_bit(self):
        self.assertEqual(Word(0x3a1c, 0x13bc, 0x84de, bit=16), 0x3a1c13bc84de)

    def test_word_raises_error_when_bit_too_small_for_representation(self):
        with self.assertRaises(ValueError):
            Word(0b10, bit=1)
        with self.assertRaises(ValueError):
            Word(0x10, bit=2)
        with self.assertRaises(ValueError):
            Word(0xF, bit=3)  # 15 needs at least four bits
        with self.assertRaises(ValueError):
            Word(0x10, bit=4)  # 16 needs at least five bits
