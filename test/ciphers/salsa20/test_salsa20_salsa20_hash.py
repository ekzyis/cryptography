# noinspection PyUnresolvedReferences
import test.context
from ciphers.stream.salsa20 import salsa20_hash
from test.helper import BitsTestCase
from util.bitseq import bitseq, bitseq8, bitseq512


class TestSalsa20CSalsa20Hash(BitsTestCase):
    def test_salsa20_salsa20_hash(self):
        x1 = bitseq(0x0, bit=512)
        z1 = bitseq(0x0, bit=512)
        self.assertEqual(salsa20_hash(x1), z1)
        x2 = bitseq8(
            (211, 159, 13, 115), (76, 55, 82, 183), (3, 117, 222, 37), (191, 187, 234, 136),
            (49, 237, 179, 48), (1, 106, 178, 219), (175, 199, 166, 48), (86, 16, 179, 207),
            (31, 240, 32, 63), (15, 83, 93, 161), (116, 147, 48, 113), (238, 55, 204, 36),
            (79, 201, 235, 79), (3, 81, 156, 47), (203, 26, 244, 243), (88, 118, 104, 54),
        )
        z2 = bitseq8(
            (109, 42, 178, 168), (156, 240, 248, 238), (168, 196, 190, 203), (26, 110, 170, 154),
            (29, 29, 150, 26), (150, 30, 235, 249), (190, 163, 251, 48), (69, 144, 51, 57),
            (118, 40, 152, 157), (180, 57, 27, 94), (107, 42, 236, 35), (27, 111, 114, 114),
            (219, 236, 232, 135), (111, 155, 110, 18), (24, 232, 95, 158), (179, 19, 48, 202),
        )
        self.assertEqual(salsa20_hash(x2), z2)
        x3 = bitseq8(
            (88, 118, 104, 54), (79, 201, 235, 79), (3, 81, 156, 47), (203, 26, 244, 243),
            (191, 187, 234, 136), (211, 159, 13, 115), (76, 55, 82, 183), (3, 117, 222, 37),
            (86, 16, 179, 207), (49, 237, 179, 48), (1, 106, 178, 219), (175, 199, 166, 48),
            (238, 55, 204, 36), (31, 240, 32, 63), (15, 83, 93, 161), (116, 147, 48, 113),
        )
        z3 = bitseq8(
            (179, 19, 48, 202), (219, 236, 232, 135), (111, 155, 110, 18), (24, 232, 95, 158),
            (26, 110, 170, 154), (109, 42, 178, 168), (156, 240, 248, 238), (168, 196, 190, 203),
            (69, 144, 51, 57), (29, 29, 150, 26), (150, 30, 235, 249), (190, 163, 251, 48),
            (27, 111, 114, 114), (118, 40, 152, 157), (180, 57, 27, 94), (107, 42, 236, 35),
        )
        self.assertEqual(salsa20_hash(x3), z3)

    def test_salsa20_salsa20_hash_raises_value_error_if_input_not_512_bit(self):
        self.assert_fn_raises_if_arguments_not_of_given_lengths(
            fn=salsa20_hash, correct_args=[bitseq512(0x0)], error=ValueError
        )
