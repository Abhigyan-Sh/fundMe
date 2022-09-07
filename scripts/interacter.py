from brownie import FundMe
from scripts.helpful_scripts import get_account
def fund():
    fundme= FundMe[-1]
    account= get_account()
    entrance_fee= fundme.getEntranceFee()
    fundme.fund({"from":account, "value":entrance_fee})

def withdraw():
    fundme= FundMe[-1]
    account= get_account()
    fundme.withdraw({"from":account})

def main():
    fund()
    withdraw()
