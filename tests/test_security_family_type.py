import unittest

from pyasx.security_family_type import SecurityFamilyType


class SecurityFamilyTypeTestCase(unittest.TestCase):
    def test_correct_values(self):
        debt: SecurityFamilyType = SecurityFamilyType.DEBT
        equity: SecurityFamilyType = SecurityFamilyType.EQUITY
        derivative: SecurityFamilyType = SecurityFamilyType.DERIVATIVE
        hybrid: SecurityFamilyType = SecurityFamilyType.HYBRID

        self.assertEqual(debt.value, 'debt')  # add assertion here
        self.assertEqual(equity.value, 'equity')  # add assertion here
        self.assertEqual(derivative.value, 'derivative')  # add assertion here
        self.assertEqual(hybrid.value, 'hybrid')  # add assertion here
