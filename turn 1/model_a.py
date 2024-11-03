import unittest
from behave import given, when, then, use_step_matcher
from financial_modeling import FinancialModel, DataIntegrityError

use_step_matcher("parse")


class TestDataIntegrityVerification(unittest.TestCase):

    @given('a financial model with initial data')
    def setUp(self):
        self.model = FinancialModel()
        self.model.data = {
            'revenue': [100, 200, 300],
            'expense': [50, 60, 70]
        }

    @when('I verify data integrity')
    def test_verify_data_integrity(self):
        self.model.verify_data_integrity()

    @then('the data integrity check passes')
    def assert_data_integrity_passes(self):
        pass  # Assertion is implicit in the absence of an exception


if __name__ == '__main__':
    unittest.main()
