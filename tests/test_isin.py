import unittest

from pyasx.isin import ISIN


class ISINTestCase(unittest.TestCase):
    def test_country_code(self):
        isin = ISIN(isin='AU0000068413')
        self.assertEqual(isin.country_code, 'AU')

    def test_check_digit(self):
        isin = ISIN(isin='AU0000068413')
        self.assertEqual(isin.check_digit, '3')

    def test_security_identifier(self):
        isin = ISIN(isin='AU0000068413')
        self.assertEqual(isin.security_identifier, '000006841')

    def test_isin_length_validation(self):
        with self.assertRaises(ValueError):
            isin = ISIN(isin='XX012345678')

    def test_isin_string_representation(self):
        isin = ISIN(isin='AU0000068413')
        self.assertEqual(str(repr(isin)), 'ISIN(isin=AU0000068413)')

    def test_isin_print_representation(self):
        isin = ISIN(isin='AU0000068413')
        self.assertEqual(str(isin), 'ISIN=AU0000068413')
