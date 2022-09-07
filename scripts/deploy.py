from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_NETWORK, deploy_mocks
from brownie import FundMe, network, config, MockV3Aggregator

def deployer():
    if network.show_active() not in LOCAL_BLOCKCHAIN_NETWORK:
        priceFeed= config["networks"][network.show_active()]["priceFeed"]
    else:
        deploy_mocks()
        priceFeed= MockV3Aggregator[-1].address

    fundme= FundMe.deploy(priceFeed,{"from":get_account()},publish_source= config["networks"][network.show_active()]["verify"])
    return fundme
def main():
    deployer()

# issue:
# cannot import name 'MockV3Aggregator' from 'brownie'
# more:
# the networks name in yaml file must start with small letters like rinkeby
# environment variables have fixed names like in this file 
# source .env refreshes env. vari.
# with test_ you deploy contract on blockchain again
# with others you might use sm.cont.[-1]

# cmd the host who is a fork 
# to give the mnemonic of ten accounts
# through the port