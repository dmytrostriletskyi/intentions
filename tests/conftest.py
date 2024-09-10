import os
import pytest


@pytest.fixture
def remove_intentions_json():
    intentions_json = './.intentions/intentions.json'

    yield intentions_json

    if os.path.exists(intentions_json):
        os.remove(intentions_json)
