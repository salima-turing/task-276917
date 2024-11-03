import pytest
from pytest_bdd import given, when, then, scenario

class FinancialModel:
    def __init__(self):
        self.data = {}

    def add_transaction(self, account, amount):
        if account not in self.data:
            self.data[account] = 0
        self.data[account] += amount

    def check_data_integrity(self):
        # Simple check for negative balances in all accounts
        for account, balance in self.data.items():
            if balance < 0:
                return False
        return True

@pytest.fixture
def model():
    return FinancialModel()

@scenario('features/data_integrity.feature', 'Verify data integrity check')
def test_data_integrity():
    pass

@given('a financial model with transactions')
def model_with_transactions(model):
    model.add_transaction('Savings', 100)
    model.add_transaction('Checking', -50)
    model.add_transaction('Investments', 75)

@when('I check the data integrity')
def check_data_integrity(model):
    model.check_data_integrity()

@then('the data integrity check should pass')
def data_integrity_should_pass(model):
    assert model.check_data_integrity(), "Data integrity check failed"
