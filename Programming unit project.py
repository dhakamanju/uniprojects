#Task 1
Code that manages the scores for a computer game and prints the leaderboard.
"""

class ScoreEntry:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def get_score(score_entry):
    return score_entry.score


class Scoreboard:
    def __init__(self):
        self.scores = []

    def add_score(self, name, score):
        self.scores.append(ScoreEntry(name, score))

    def print_leaderboard(self):
        sorted_scores = sorted(self.scores, key=get_score, reverse=True)
        top_three = sorted_scores[:3]
        for score_entry in top_three:
            print(f'{score_entry.name}: {score_entry.score}')


scoreboard = Scoreboard()
scoreboard.add_score('Alice', 7821)
scoreboard.add_score('Bob', 12103)
scoreboard.add_score('Charlie', 8762)
scoreboard.add_score('Denise', 6573)
scoreboard.print_leaderboard()

"""#Task 2
Write a simple program to track time spent on miscellaneous chores.
"""

class ChoreTracker:
    def __init__(self):
        self.chores = {}

    def add_hours(self, chore, hours):
        if chore in self.chores:
            self.chores[chore] += hours
        else:
            self.chores[chore] = hours

    def print_summary(self):
        total_hours = 0
        for chore, hours in self.chores.items():
            print(f'{chore}: {hours:.2f} hours')
            total_hours += hours
        print(f'TOTAL: {total_hours:.2f} hours')


tracker = ChoreTracker()

tracker.add_hours('sweeping', 0.75)
tracker.add_hours('laundry', 0.5)
tracker.add_hours('working', 6)
tracker.add_hours('mopping', 0.5)
tracker.add_hours('laundry', 1)
tracker.add_hours('working', 5.5)

tracker.print_summary()

"""#Task 3 A
Write code that handles the transfer of funds from one bank account to another.
"""

class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount


def print_balances(account_a, account_b):
    print('== Account balances ==')
    print(f'  {account_a.name}: ${account_a.balance:.2f}')
    print(f'  {account_b.name}: ${account_b.balance:.2f}')


def transfer_funds(amount, from_account, to_account):
    from_account.withdraw(amount)
    to_account.deposit(amount)


account_a = BankAccount('Alice', 100)
account_b = BankAccount('Bob', 100)
print_balances(account_a, account_b)

another_transfer = 'y'
while another_transfer == 'y':
    amount = float(input('Enter transfer amount ($): '))

    transfer_funds(amount, account_a, account_b)

    print_balances(account_a, account_b)
    another_transfer = input('Perform another transfer? (y/n): ')

"""#Task 3 B

"""

class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Balance would be negative after withdrawal")
        else:
            self.balance = self.balance - amount

def print_balances(account_a, account_b):
    print('== Account balances ==')
    print(f'  {account_a.name}: ${account_a.balance:.2f}')
    print(f'  {account_b.name}: ${account_b.balance:.2f}')

def transfer_funds(amount, from_account, to_account):
    from_account.withdraw(amount)
    to_account.deposit(amount)

account_a = BankAccount('Alice', 100)
account_b = BankAccount('Bob', 100)
print_balances(account_a, account_b)

another_transfer = 'y'
while another_transfer == 'y':
    amount = float(input('Enter transfer amount ($): '))

    transfer_funds(amount, account_a, account_b)

    print_balances(account_a, account_b)
    another_transfer = input('Perform another transfer? (y/n): ')

"""#Task 3 C"""

class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"<< Error transferring Funds >>")
        self.balance = self.balance - amount

def print_balances(account_a, account_b):
    print('== Account balances ==')
    print(f'  {account_a.name}: ${account_a.balance:.2f}')
    print(f'  {account_b.name}: ${account_b.balance:.2f}')

def transfer_funds(amount, from_account, to_account):
    from_account.withdraw(amount)
    to_account.deposit(amount)

account_a = BankAccount('Alice', 100)
account_b = BankAccount('Bob', 100)
print_balances(account_a, account_b)

another_transfer = 'y'
while another_transfer == 'y':
    amount = float(input('Enter transfer amount ($): '))

    try:
        transfer_funds(amount, account_a, account_b)
    except ValueError as e:
        print(e)

    print_balances(account_a, account_b)
    another_transfer = input('Perform another transfer? (y/n): ')

"""#Task 4 A"""

import pandas as pd

URL= 'https://gist.githubusercontent.com/anibali/c2abc8cab4a2f7b0a6518d11a67c693c/raw/3b1bb5264736bb762584104c9e7a828bef0f6ec8/penguins.csv'

df = pd.read_csv (URL)
 print (df.head ( ))

df.groupby('species').mean(numeric_only=True)

"""#Task 4 B"""

import matplotlib.pyplot as plt

adelie = df[df['species'] == 'Adelie']
chinstrap = df[df['species'] == 'Chinstrap']
gentoo = df[df['species'] == 'Gentoo']

plt.figure(figsize=(10, 6))
plt.scatter(adelie['body_mass_g'], adelie['bill_length_mm'], color='red', label='Adelie')
plt.scatter(chinstrap['body_mass_g'], chinstrap['bill_length_mm'], color='grey', label='Chinstrap')
plt.scatter(gentoo['body_mass_g'], gentoo['bill_length_mm'], color='blue', label='Gentoo')

plt.title('Penguin measurements by species')
plt.xlabel('Body mass (g)')
plt.ylabel('Bill length (mm)')

plt.legend()
plt.show()

"""#Task 4 C"""

df['bill_proportion'] = df['bill_length_mm'] / df['bill_depth_mm']

adelie = df[df['species'] == 'Adelie']
chinstrap = df[df['species'] == 'Chinstrap']
gentoo = df[df['species'] == 'Gentoo']

plt.figure(figsize=(10, 6))
plt.scatter(adelie['body_mass_g'], adelie['bill_proportion'], color='red', label='Adelie')
plt.scatter(chinstrap['body_mass_g'], chinstrap['bill_proportion'], color='grey', label='Chinstrap')
plt.scatter(gentoo['body_mass_g'], gentoo['bill_proportion'], color='blue', label='Gentoo')

plt.title('Penguin proportions by species')
plt.xlabel('Body mass (g)')
plt.ylabel('Bill proportion (length/width)')

plt.legend()
plt.show()
