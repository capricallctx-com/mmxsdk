from unittest import TestCase

import wallet


class Test(TestCase):
    def test_get_balances(self):
        balance = wallet.get_balances()
        if balance is None:
            self.fail()

