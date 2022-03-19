from random import random
import pytest
from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible(
    # get_keyhash,
    # chainlink_fee,
):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    requestId = creation_transaction.events["RequestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )
    # Assert
    assert advanced_collectible.tokenCounter() > 0
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3

    # advanced_collectible = AdvancedCollectible.deploy(
    #     get_contract("vrf_coordinator").address,
    #     get_contract("link_token").address,
    #     get_keyhash,
    #     {"from": get_account()},
    # )
    # get_contract("link_token").transfer(
    #     advanced_collectible.address, chainlink_fee * 3, {"from": get_account()}
    # )
    # # Act
    # transaction_receipt = advanced_collectible.createCollectible(
    #     "None", {"from": get_account()}
    # )
    # requestId = transaction_receipt.events["RequestedCollectible"]["requestId"]
    # assert isinstance(transaction_receipt.txid, str)
    # get_contract("vrf_coordinator").callBackWithRandomness(
    #     requestId, 777, advanced_collectible.address, {"from": get_account()}
    # )
    # # Assert
    # assert advanced_collectible.tokenCounter() > 0
    # assert isinstance(advanced_collectible.tokenCounter(), int)
