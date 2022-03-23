from random import random
import pytest
import time
from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration(
    # get_keyhash,
    # chainlink_fee,
):
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(300)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
