import pytest



def test_base_configurator_not_implemented(app, test_not_implemented_configurator):
    with pytest.raises(NotImplementedError):
        test_not_implemented_configurator(app).configure_wrapper()

def test_base_configurator_failing(app, test_failing_configurator):
    test_failing_configurator.ExitOnError = True
    with pytest.raises(ValueError):
        test_failing_configurator(app).configure_wrapper()
    test_failing_configurator.ExitOnError = False
    test_failing_configurator(app).configure_wrapper()
    

