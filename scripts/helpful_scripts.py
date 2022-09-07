from brownie import MockV3Aggregator, network, accounts, config
LOCAL_BLOCKCHAIN_NETWORK= ["development", "ganache-local"]
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_NETWORK:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

DECIMALS= 8
INITIAL_ANSWER= 2000000000000000000
def deploy_mocks():
    if len(MockV3Aggregator)== 0:
        MockV3Aggregator.deploy(DECIMALS, INITIAL_ANSWER, {"from":get_account()})
    print("priceFeed deployed!")
