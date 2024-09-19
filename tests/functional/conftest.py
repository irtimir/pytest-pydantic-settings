import pytest

from tests.functional.settings import SomeSettings


@pytest.fixture
def config():
    return SomeSettings()
