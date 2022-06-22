import pytest

from src.base_configurator import BaseConfigurator

class TestFailingConfigurator(BaseConfigurator):
    def configure(self):
        raise ValueError("Configurator Failed")

class TestSucceedingConfigurator(BaseConfigurator):
    def configure(self):
        pass



@pytest.fixture
def test_failing_configurator():
    return TestFailingConfigurator


@pytest.fixture
def test_succeeding_configurator():
    return TestSucceedingConfigurator