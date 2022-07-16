"""
main.py
"""
import datetime
from enum import Enum
from typing import NamedTuple
from decimal import Decimal
from dataclasses import dataclass


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


class Account:
    """Represents a budget account

    The user can add transactions on a specific account.
    Example of transactions: Income, Expenses.

    Each account has a type. Cash, Checking, Credit card.
    """

    acc_type: AccountType = AccountType.CHECKING

    def __init__(self, acc_name: str, acc_ammount: Decimal = Decimal(0)) -> None:
        self.acc_name = acc_name
        self.acc_ammount = acc_ammount


class Activity(NamedTuple):
    """Represent an activity over a category

    This class tracks the activities over a category budget
    """

    available: int = 0


class Category(NamedTuple):
    """Represents a budget category

    The category is used unde add new transaction.
    The transaction should be for a specific account for one category.
    """

    name: str
    activity: Activity = Activity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"


@dataclass
class Transaction:
    """Represents a transaction entry

    A transaction ca be added for many accounts.
    Also, a transaction can be added for a specific category
    """

    account: Account
    category: Category
    payee: str = ""
    inflow: Decimal = Decimal(0)
    outflow: Decimal = Decimal(0)
    date: datetime.date = datetime.date.today()

    def __post_init__(self):
        if self.inflow:
            self.account.acc_ammount += self.inflow
        if self.outflow:
            self.account.acc_ammount -= self.outflow
