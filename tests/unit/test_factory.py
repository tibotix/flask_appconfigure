import pytest

from src.exceptions import AppConfigurationException
from src.factory import  ConfiguratorPool, ApplicationFactory

def test_configurator_pool(test_succeeding_configurator):
    pool = ConfiguratorPool()
    pool.add_configurator(test_succeeding_configurator, args=(1,), kwargs={"key":"value"})
    configurator_information = pool.get_configuration_information()
    assert len(configurator_information) == 1
    configurator_information = configurator_information[0]
    assert configurator_information.configurator_class == test_succeeding_configurator
    assert configurator_information.args == (1,)
    assert configurator_information.kwargs == {"key": "value"}



def test_application_factory_create_app(test_succeeding_configurator):
    pool = ConfiguratorPool()
    pool.add_configurator(test_succeeding_configurator, kwargs={"value": 1})
    factory = ApplicationFactory(pool)
    app = factory.create_app("import_name", template_folder="my_template_folder")
    assert app.modified == 1
    assert app.import_name == "import_name"
    assert app.template_folder == "my_template_folder"

def test_application_factory_configure_app(app, test_succeeding_configurator):
    pool = ConfiguratorPool()
    pool.add_configurator(test_succeeding_configurator)
    factory = ApplicationFactory(pool)
    app.modified_before = True
    app = factory.configure_app(app)
    assert app.modified == True
    assert app.modified_before == True

def test_application_factory_failing(test_failing_configurator):
    pool = ConfiguratorPool()
    test_failing_configurator.ExitOnError = True
    pool.add_configurator(test_failing_configurator)
    factory = ApplicationFactory(pool)
    with pytest.raises(AppConfigurationException):
        app = factory.create_app()
    test_failing_configurator.ExitOnError = False