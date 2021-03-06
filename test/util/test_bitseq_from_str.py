import bitstring

# noinspection PyUnresolvedReferences
import test.context
from test.helper import BitsTestCase
from util.bitseq import bitseq_from_str


class TestBitSeq(BitsTestCase):

    def test_bitseq_from_str_returns_bitstring_Bits_instance(self):
        b = bitseq_from_str("0x1", "0x2", "0x3", "0x4")
        self.assertIsInstance(b, bitstring.Bits)

    def test_bitseq_from_str(self):
        b1 = bitseq_from_str("0x1", "0x2", "0x3", "0x4")
        self.assertBit(b1, 0x1234, 16)
        b2 = bitseq_from_str("0x01", "0x02", "0x03", "0x04")
        self.assertBit(b2, 0x01020304, 32)

    def test_bitseq_from_str_with_zero_bits(self):
        # leading zeros
        b1 = bitseq_from_str("0x0", "0x0", "0xa", "0xf")
        self.assertBit(b1, 0xaf, 16)
        # only zeros
        b2 = bitseq_from_str("0x0", "0x0", "0x0", "0x0")
        self.assertBit(b2, 0x0, 16)

    def test_bitseq_from_str_with_tuple_notation(self):
        b1 = bitseq_from_str(("0x0",) * 4)
        self.assertBit(b1, 0x0, 16)
        b2 = bitseq_from_str("0x1", ("0x0",) * 3)
        self.assertBit(b2, 0x1000, 16)

    def test_bitseq_from_str_with_mixed_amount_of_bits(self):
        b1 = bitseq_from_str("0x10", "0xf")
        self.assertBit(b1, 0x10f, 12)
        b2 = bitseq_from_str("0x0001", "0x00f0")
        self.assertBit(b2, 0x100f0, 32)

    def test_bitseq_from_str_with_specified_bit(self):
        b1 = bitseq_from_str("0x0", "0x0", bit=8)
        self.assertBit(b1, 0x0000, 16)
        b2 = bitseq_from_str("0x1f", "0x0f", bit=16)
        self.assertBit(b2, 0x001f000f, 32)

    def test_bitseq_from_str_raises_value_error_if_integer_too_large(self):
        with self.assertRaises(ValueError):
            bitseq_from_str("0xf", bit=3)
        with self.assertRaises(ValueError):
            bitseq_from_str("0x10", bit=4)
