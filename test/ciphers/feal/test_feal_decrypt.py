# noinspection PyUnresolvedReferences
import test.context
# noinspection PyProtectedMember
from ciphers.block.feal import decrypt, _decrypt_preprocessing, _decrypt_iterative_calculation
from test.helper import BitsTestCase
from util.bitseq import bitseq128, bitseq64, bitseq16, bitseq32


class TestFEALDecrypt(BitsTestCase):

    def test_feal_decrypt_raises_value_error_if_text_not_64_bit_or_key_not_128_bit(self):
        self.assert_fn_raises_if_arguments_not_of_given_lengths(
            fn=decrypt, correct_args=[bitseq128(0x0), bitseq64(0x0)], error=ValueError
        )

    def test_feal_decrypt_matches_specification_in_paper(self):
        """Checks that the FEAL decryption decrypts the given ciphertext."""
        # i/o values taken from test for encrypt.
        #   Since decryption should reverse encryption, I assume I can
        #   just pass in the output of encrypt into the input of decrypt
        #   and expect the input of encrypt as output of decrypt.
        c = bitseq64(0x9C9B54973DF685F8)
        k = bitseq128(0x123456789ABCDEF0123456789ABCDEF)
        p = decrypt(k, c)
        self.assertEqual(p, "0x0000000000000000")

    def test_feal_decrypt_preprocessing_matches_specification_in_paper(self):
        # i/o values taken from test for encrypt.
        #   As specified in the paper, the concatenation of the keys r_n, l_n which were calculated
        #   during encryption should be returned when using the output of said encryption as input.
        k34, k35, k36, k37 = bitseq16(0x9F72), bitseq16(0x6643), bitseq16(0xAD32), bitseq16(0x683A)
        c = bitseq64(0x9C9B54973DF685F8)
        out = _decrypt_preprocessing([k34, k35, k36, k37], c)
        self.assertEqual(out, "0x03E932D4932DDF16")

    def test_feal_decrypt_iterative_calculation_matches_specification_in_paper(self):
        # i/o values taken from test for encrypt.
        #   As specified in the paper, the same l and r keys should be created as during encryption
        #   when using the same key (here assured by using same subkeys) and the resulting ciphertext
        #   (here assured by defining ln and rn key, which would be calculated from the decryption input).
        ln, rn = bitseq32(0x932DDF16), bitseq32(0x03E932D4)
        sk = [
            bitseq16(0x7519), bitseq16(0x71F9), bitseq16(0x84E9), bitseq16(0x4886),
            bitseq16(0x88E5), bitseq16(0x523B), bitseq16(0x4EA4), bitseq16(0x7ADE),
            bitseq16(0xFE40), bitseq16(0x5E76), bitseq16(0x9819), bitseq16(0xEEAC),
            bitseq16(0x1BD4), bitseq16(0x2455), bitseq16(0xDCA0), bitseq16(0x653B),
            bitseq16(0x3E32), bitseq16(0x4652), bitseq16(0x1CC1), bitseq16(0x34DF),
            bitseq16(0x778B), bitseq16(0x771D), bitseq16(0xD324), bitseq16(0x8410),
            bitseq16(0x1CA8), bitseq16(0xBC64), bitseq16(0xA0DB), bitseq16(0xBDD2),
            bitseq16(0x1F5F), bitseq16(0x8F1C), bitseq16(0x6B81), bitseq16(0xB560),
            bitseq16(0x196A), bitseq16(0x9AB1), bitseq16(0xE015), bitseq16(0x8190),
            bitseq16(0x9F72), bitseq16(0x6643), bitseq16(0xAD32), bitseq16(0x683A),
        ]
        l, r = list(_decrypt_iterative_calculation(ln, rn, sk))
        self.assertEqual(l[0], "0x196A9AB1")
        self.assertEqual(l[1], "0xF97F1B21")
        self.assertEqual(l[2], "0x4C3667CD")
        self.assertEqual(l[3], "0xDE025865")
        self.assertEqual(l[4], "0x068245EF")
        self.assertEqual(l[5], "0x69E51495")
        self.assertEqual(l[6], "0x3E276105")
        self.assertEqual(l[7], "0xDA4B207D")
        self.assertEqual(l[8], "0x3B40E0FA")
        self.assertEqual(l[9], "0x83505F94")
        self.assertEqual(l[10], "0x9EA62593")
        self.assertEqual(l[11], "0x6BCC2E80")
        self.assertEqual(l[12], "0xB7797FFC")
        self.assertEqual(l[13], "0x888DEF7A")
        self.assertEqual(l[14], "0x93F874E6")
        self.assertEqual(l[15], "0x37D163B7")
        self.assertEqual(l[16], "0x4446BCE4")
        self.assertEqual(l[17], "0xFAFE290B")
        self.assertEqual(l[18], "0xD86B48E4")
        self.assertEqual(l[19], "0x542D6EBB")
        self.assertEqual(l[20], "0x2C82BF2A")
        self.assertEqual(l[21], "0x5BBAE971")
        self.assertEqual(l[22], "0x3828498B")
        self.assertEqual(l[23], "0x0EA71A8C")
        self.assertEqual(l[24], "0x339CD013")
        self.assertEqual(l[25], "0xC65851F1")
        self.assertEqual(l[26], "0xE0B20838")
        self.assertEqual(l[27], "0x7155D40B")
        self.assertEqual(l[28], "0xBE94A0EA")
        self.assertEqual(l[29], "0x8895B53A")
        self.assertEqual(l[30], "0xE1DBDC34")
        self.assertEqual(l[31], "0xA63FCF84")
        self.assertEqual(l[32], "0x932DDF16")
        self.assertListEqual(l[1:], r[:-1])
        self.assertEqual(r[32], "0x03E932D4")
