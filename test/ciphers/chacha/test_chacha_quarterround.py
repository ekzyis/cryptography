# noinspection PyUnresolvedReferences
import test.context
from ciphers.stream.chacha import quarterround, quarterround_state
from test.helper import BitsTestCase
from util.bitseq import bitseq32, bitseq128, bitseq512


class TestChaChaQuarterround(BitsTestCase):
    def test_chacha_quarterround(self):
        self.assertEqual(
            quarterround(bitseq32(0x11111111, 0x01020304, 0x9b8d6f43, 0x01234567)),
            bitseq32(0xea2a92f4, 0xcb1cf8ce, 0x4581472e, 0x5881c4bb)
        )

    def test_chacha_quarterround_raises_value_error_if_input_not_128_bit(self):
        self.assert_fn_raises_if_arguments_not_of_given_lengths(
            fn=quarterround, correct_args=[bitseq128(0x0)], error=ValueError
        )

    def test_chacha_quarterround_on_state(self):
        state = bitseq32(
            0x879531e0, 0xc5ecf37d, 0x516461b1, 0xc9a62f8a,
            0x44c20ef3, 0x3390af7f, 0xd9fc690b, 0x2a5f714c,
            0x53372767, 0xb00a5631, 0x974c541a, 0x359e9963,
            0x5c971061, 0x3d631689, 0x2098d9d6, 0x91dbd320,
        )
        new_state = bitseq32(
            0x879531e0, 0xc5ecf37d, 0xbdb886dc, 0xc9a62f8a,
            0x44c20ef3, 0x3390af7f, 0xd9fc690b, 0xcfacafd2,
            0xe46bea80, 0xb00a5631, 0x974c541a, 0x359e9963,
            0x5c971061, 0xccc07c79, 0x2098d9d6, 0x91dbd320
        )
        self.assertEqual(quarterround_state(state, 2, 7, 8, 13), new_state)

    def test_chacha_quarterround_state_raises_value_error_if_state_not_512_bit(self):
        self.assert_fn_raises_if_arguments_not_of_given_lengths(
            fn=quarterround_state, correct_args=[bitseq512(0x0), 0, 0, 0, 0], arg_index_to_check=0, error=ValueError
        )
