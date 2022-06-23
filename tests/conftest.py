import pytest
import flask

from src.base_configurator import BaseConfigurator


class TestNotImplementedConfigurator(BaseConfigurator):
    pass

class TestFailingConfigurator(BaseConfigurator):
    def configure(self):
        raise ValueError("Configurator Failed")

class TestSucceedingConfigurator(BaseConfigurator):
    def configure(self, value=True):
        self.app.modified = value


@pytest.fixture
def app():
    return flask.Flask(__name__)

@pytest.fixture
def test_not_implemented_configurator():
    return TestNotImplementedConfigurator

@pytest.fixture
def test_failing_configurator():
    return TestFailingConfigurator


@pytest.fixture
def test_succeeding_configurator():
    return TestSucceedingConfigurator