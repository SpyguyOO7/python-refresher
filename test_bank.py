#from bank import Account
import bank
import unittest

class TestHello(unittest.TestCase):
    def test_init(self):
        account = bank.Account(0,"bobby",123)
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.name, "bobby")
        self.assertEqual(account.number, 123)

    def test_deposit(self):
        account = bank.Account(0,"bobby",123)
        self.assertEqual(account.balance, 0)
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = bank.Account(200,"bobby",123)
        self.assertEqual(account.balance, 200)
        account.withdraw(100)
        self.assertEqual(account.balance, 100)

    # def test_print(self):
    #     account = bank.Account(0,"bobby",123)
    #     self.assertEqual(print(account), 0)

if __name__ == "__main__":
    unittest.main()
