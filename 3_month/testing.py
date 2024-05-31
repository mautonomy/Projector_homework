import unittest

# Code from Lesson 14

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < (self.overdraft_limit * -1):
            print(f"Overdraft letter sent for Account {self.account_number}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account):
        self.accounts[account.account_number] = account

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def pay_dividend(self, dividend_amount):
        for account in self.accounts.values():
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts.values():
            print(account)


# Test Code

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):

        account_number = 12345
        initial_balance = 1000.0
        account = Account(account_number, initial_balance)

        self.bank.open_account(account)

        self.assertIn(account_number, self.bank.accounts)

        self.assertEqual(self.bank.accounts[account_number].balance, initial_balance)

        print(self.bank.accounts[account_number])


if __name__ == '__main__':
    unittest.main()


# Task 2

import unittest
from unittest.mock import patch


# Code from Lesson 14

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self.balance < (self.overdraft_limit * -1):
            print(f"Overdraft letter sent for Account {self.account_number}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account):
        self.accounts[account.account_number] = account

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def pay_dividend(self, dividend_amount):
        for account in self.accounts.values():
            account.deposit(dividend_amount)

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()

    def show_accounts(self):
        for account in self.accounts.values():
            print(account)


# Test Code

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        account_number = 12345
        initial_balance = 1000.0
        account = Account(account_number, initial_balance)

        self.bank.open_account(account)

        self.assertIn(account_number, self.bank.accounts)

        self.assertEqual(self.bank.accounts[account_number].balance, initial_balance)

        print(self.bank.accounts[account_number])

    @patch('builtins.print')
    def test_update_accounts(self, mock_print):
        savings_account = SavingsAccount(12345, 1000.0, 5.0)  # 5% interest rate
        current_account = CurrentAccount(67890, -500.0, 200)  # -200 overdraft limit

        self.bank.open_account(savings_account)
        self.bank.open_account(current_account)

        self.bank.update_accounts()

        self.assertEqual(self.bank.accounts[12345].balance, 1050.0)  # 1000 + 5% of 1000

        mock_print.assert_called_with('Overdraft letter sent for Account 67890')


if __name__ == '__main__':
    unittest.main()

