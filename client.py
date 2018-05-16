from model import *
from threading import Thread
import time
import random
import string

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

session = Session()


def addBet(name, money, bet):
    money = money - bet
    user = session.query(User).filter_by(name=name).first()
    if user:
        user.personal_account = user.personal_account + money
        user.prize_fund_account = user.prize_fund_account + bet
        session.commit()
    else:
        session.add(
            User(id=identifier.__next__(), name=name, personal_account=money, prize_fund_account=bet, prize_fund=fund))
        session.commit()


def make_identifier():
    i = 0
    while True:
        i += 1
        yield i


def sum_fund(fund):
    while True:
        fund.jackpot = sum([i.prize_fund_account for i in fund.users])
        time.sleep(5)


def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word


def generate_user():
    status = True
    while status:
        name = generate_word(random.randint(3, 10))
        status = bool(session.query(User).filter_by(name).first())
    money = round(random.uniform(1, 20), 1)
    bet = round(random.uniform(1, money), 1)
    return name, money, bet


if __name__ == '__main__':
    identifier = make_identifier()
    fund = PrizFund(id=identifier.__next__(), name='My Prize Fund')
    thread = Thread(target=sum_fund, args=({'fund': fund}))
    thread.start()
    while True:
        addBet(*generate_user())
        time.sleep(1)
