"""
Tests for accounts classes.
"""
import datetime
import pytest

from budgetcli.models import Account, AccountType, Category, Transaction


@pytest.fixture
def get_categories() -> list[Category]:
    """Return a list of categories"""
    names = ["Fun", "Groceries", "Internet"]
    categories = [Category(name) for name in names]
    return categories


class TestAccountsModel:
    """Contains all the tests for account model"""

    def test_account_name(self):
        """Test the instace of the account class"""
        account = Account(acc_name="cash")
        assert account.acc_name == "cash"

    def test_account_type(self):
        """Test the account type.

        It should have a default value..
        """
        account = Account("cash")
        assert account.acc_type == AccountType.CHECKING

    def test_account_ammount(self):
        """Test the account ammount

        It should have a value of 0 if not set.
        """
        account = Account("cash")
        assert account.acc_ammount == 0


class TestCategoriesModel:
    """Contains all the tests for the category model"""

    def test_category_name(self):
        """Test the category name"""
        category = Category(name="Shoping")
        assert category.name == "Shoping"

    def test_category_empty_name(self):
        """Test if category is created without providing name
        It should raise TypeError
        """
        with pytest.raises(TypeError):
            Category()

    def test_category_representation(self):
        """Test the string repr"""
        category = Category(name="Shoping")
        assert repr(category) == "Category(name=Shoping)"


class TestTransactionsModel:
    """Contains all the tests for the transaction model"""

    def test_create_new_transaction(self):
        """Test creating new transaction"""

        account = Account("Wallet", 200)
        category = Category(name="Groceries")
        Transaction(account=account, category=category, inflow=50)
        Transaction(account=account, category=category, outflow=20)
        Transaction(account=account, category=category, inflow=10)

        assert account.acc_ammount == 240
