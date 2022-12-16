import os

from brownie import Contract, StarknetERC20Bridge, accounts


L1_BRIDGE_ADDRESS = os.environ.get("PARACLEAR_L1_BRIDGE_ADDRESS")
L1_USER_ADDRESS = os.environ.get("PARACLEAR_L1_USER_ADDRESS")


def main():
    """
    Add funds to user accounts.
    Requirement: All accounts must be preloaded on brownie
    before running the deploy script.
    """

    admin_account = accounts.load("admin")

    from_admin_account = {"from": admin_account}

    bridge = Contract.from_abi(
        "StarknetERC20Bridge",
        L1_BRIDGE_ADDRESS,
        StarknetERC20Bridge.abi,
    )

    # 100,000 USDC with 6 decimals
    amount = 100000000000

    tx = bridge.withdraw(amount, L1_USER_ADDRESS, from_admin_account)

    print("withdraw ", tx)