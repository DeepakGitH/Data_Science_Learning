
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create ad new crdit card instance

        The initial balance is zero
        It has customer
        bank
        acnt

        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._balance = 0
        self._limit = limit


    def get_customer(self):
        """Return the customer name"""
        return self._customer

    def get_bank(self):
        """Return the banks name"""
        return self._bank

    def get_account(self):
        """Return accout"""
        return self._account

    def get_balance(self):
        """Return Balance"""
        return self._balance

    def charge(self, price):
        """Charge price to card assuming sufficient credit

        Return True if charge was processed; False if charge was denied

        """
        if (price + self._balance > self._limit):
            return False
        else :
            self._balance += price
            return True


    def make_payment(self, payment):
        """This function deducts from payments"""
        self._balance -= payment



class PredatoryCreditCard(CreditCard):
    """Predatory Credit Card"""

    def _init_(self, customer, bank, acnt, limit, apr):
        """New type of card
        card with fines and interests etc
        """
        super(PredatoryCreditCard, self).__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge"""
        success = super(PredatoryCreditCard, self).charge(price)
        if not success:
            self._balance += 5
        return success

