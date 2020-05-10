import unittest

# noinspection PyUnresolvedReferences
import test.context
from ciphers.feal import feal
from test.ciphers.feal.integration.wrappers import default_decrypt_args, default_encrypt_args


class TestFeal(unittest.TestCase):

    def test_integration_feal_option_mode_of_operation_ecb_with_no_remainder(self):
        @default_encrypt_args('-m', 'ecb', key='0xffff', text='0xfffafffafffafffafffafffafffafffa')
        def test_mode_of_operation_ecb_with_encrypt():
            c = feal()
            #              KEY    TEXT                 OUTPUT IN HEX
            # feal encrypt 0xffff 0xfffafffafffafffa   0xa281baaa4303e813
            self.assertEqual(hex(int(c, 0)).lower(), '0xa281baaa4303e813a281baaa4303e813')

        test_mode_of_operation_ecb_with_encrypt()

        @default_decrypt_args('-m', 'ecb', key='0xffff', text='0xa281baaa4303e813a281baaa4303e813')
        def test_mode_of_operation_ecb_with_decrypt():
            p = feal()
            self.assertEqual(hex(int(p, 0)).lower(), '0xfffafffafffafffafffafffafffafffa')

        test_mode_of_operation_ecb_with_decrypt()
