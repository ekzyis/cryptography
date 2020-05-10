import unittest

# noinspection PyUnresolvedReferences
import test.context
from ciphers.feal import feal, FEALArgumentException
from test.ciphers.feal.integration.wrappers import default_decrypt_args, default_encrypt_args


class TestFealOptionOutputFormat(unittest.TestCase):
    @default_encrypt_args('-o', 'bin')
    def test_integration_feal_encrypt_output_format_bin(self):
        c = feal()
        self.assertEqual(c, '0b1001110010011011010101001001011100111101111101101000010111111000')

    @default_decrypt_args('-o', 'bin')
    def test_integration_feal_decrypt_output_format_bin(self):
        p = feal()
        self.assertEqual(p, '0b0')

    @default_encrypt_args('-o', 'oct')
    def test_integration_feal_encrypt_output_format_oct(self):
        c = feal()
        self.assertEqual(c, '0o1162332511347575502770')

    @default_decrypt_args('-o', 'oct')
    def test_integration_feal_decrypt_output_format_oct(self):
        p = feal()
        self.assertEqual(p, '0o0')

    @default_encrypt_args('-o', 'dec')
    def test_integration_feal_encrypt_output_format_dec(self):
        c = feal()
        self.assertEqual(c, '11284706299863270904')

    @default_decrypt_args('-o', 'dec')
    def test_integration_feal_decrypt_output_format_dec(self):
        p = feal()
        self.assertEqual(p, '0')

    @default_encrypt_args('-o', 'hex')
    def test_integration_feal_encrypt_output_format_hex(self):
        c = feal()
        self.assertEqual(c, '0x9c9b54973df685f8')

    @default_decrypt_args('-o', 'hex')
    def test_integration_feal_decrypt_output_format_hex(self):
        p = feal()
        self.assertEqual(p, '0x0')

    @default_encrypt_args('-o', 'invalid')
    def test_integration_feal_encrypt_output_format_invalid_raises_error(self):
        with self.assertRaises(FEALArgumentException):
            feal()

    @default_decrypt_args('-o', 'invalid')
    def test_integration_feal_decrypt_output_format_invalid_raises_error(self):
        with self.assertRaises(FEALArgumentException):
            feal()
