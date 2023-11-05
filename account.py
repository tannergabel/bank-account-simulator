from decimal import Decimal

class Account:

    def __init__(self, account_name: str, balance: Decimal = Decimal("0.00")):
        """Initialize an Account.

        Args:
            account_name (str): Name of the account.
            balance (Decimal, optional): The initial balance of the account.
            Defaults to Decimal("0.00").
        """
        self.__name = account_name
        self.__balance = balance
    
    def set_balance(self, new_balance: Decimal) -> Decimal:
        """Sets the current balance amount.

        Args:
            new_balance (Decimal): Value to set the current balance to.

        Returns:
            Decimal: The old balance.
        """
        old = self.__balance
        self.__balance = new_balance
        return old
    
    def get_balance(self) -> Decimal:
        return self.__balance
    
    def update_balance(self, change: Decimal):
        """Increases or decreases the balance of an account.

        Args:
            change (Decimal): Amount to change a balance by.
        """
        self.__balance += change