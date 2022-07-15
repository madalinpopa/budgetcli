"""
main.py
"""
from enum import Enum

class AccountType(Enum):
    """Accounts types

    An account can be one of the below types:
    - Checking
    - Cash
    - Credit card
    """
    CHECKING: int = 1
    CREDIT: int = 3
    CASH: int = 2



class Accounts:
    """Represents a budget account

    The user can add transactions on a specific account.
    Example of transactions: Income, Expenses.

    Each account has a type. Cash, Checking, Credit card.
    """

    acc_type: AccountType = AccountType.CHECKING

    def __init__(self, acc_name: str, acc_ammount: int = 0) -> None:
        self.acc_name = acc_name
        self.acc_ammount = acc_ammount

