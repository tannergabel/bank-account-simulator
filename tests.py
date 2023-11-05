from account import Account
from decimal import Decimal

def test_account_balance_deep_copy():
    init_balance = Decimal("1.00")
    new_balance = Decimal("2.00")
    a = Account("", init_balance)
    old_balance = a.set_balance(new_balance)
    assert old_balance == init_balance
    assert a.get_balance() == new_balance