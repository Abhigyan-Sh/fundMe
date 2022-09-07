# testing the entranceFee,
# only owner can withdraw
from brownie import exceptions, accounts
from scripts.helpful_scripts import get_account
from scripts.deploy import deployer
import pytest

def test_entranceFee():
    account= get_account()
    fundme= deployer()
    entranceFee= fundme.getEntranceFee()+1000
    txn= fundme.fund({"from":account, "value":entranceFee})
    txn.wait(1)
    assert fundme.addressToAmountFunded(account.address)== entranceFee

def test_only_owner_canWithdraw():
    account= accounts.add()
    fundme= deployer()
    with pytest.raises(exceptions.VirtualMachineError):
        fundme.withdraw({"from":account})