"""
Tests for accounts classes.
"""
from src.budget import Accounts, AccountType


def test_account_name():
    """Test the instace of the account class"""
    account = Accounts(acc_name="cash")
    assert account.acc_name == "cash"


def test_account_type():
    """Test the account type.

    It should have a default value..
    """
    account = Accounts("cash")
    assert account.acc_type == AccountType.CHECKING

def test_account_ammount():
    """Test the account ammount

    It should have a value of 0 if not set.
    """
    account = Accounts("cash")
    assert account.acc_ammount == 0
