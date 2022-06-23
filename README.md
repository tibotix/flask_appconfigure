# Flask Appfactory

*Flask Appfactoy* is a simple and lightweight module which simplifies the concept
of creating and configuring Flask Applications in an Object-Oriented Way.

## Installation

You can install *Flask Appfactory* from this Github repository with `python3 setup.py install`,
or just install it directly from pypi with `pip3 install flask-appfactory`.


## Get Started

### BaseConfigurator

Flask Appfactory uses the concept of Configurators. Each configurator should do exactly one configuration.
To create a custom configurator, simply subclass from `BaseConfigurator` and implement the `configure` method.
Inside the configure method, you have access to the Flask Application through `self.app`:

```python
from flask_appfactory import BaseConfigurator

class DummyConfigurator(BaseConfigurator):
    ExitOnError = False

    def configure(self):
        self.app.before_request(lambda: print("before request"))
```

To configure wether a raised exception should abort the whole configuration process or not, you can set the `ExitOnError` attribute
of your own configurator to `True` or `False`. The default is `True`.


### ConfiguratorPool

To use your own configurators, you will need an instance of a `ConfiguratorPool`. There you can add your configurators
in exactly the same order as they are then executed.

```python
from flask_appfactoy import ConfiguratorPool, BaseConfigurator

class DummyConfigurator2(BaseConfigurator):
    def configure(self, environment="dev"):
        pass

pool = ConfiguratorPool()
pool.add_configurator(DummyConfigurator)
pool.add_configurator(DummyConfigurator2)
```

When configuring your Flask Application, the `DummyConfigurator` gets executed first, then `DummyConfigurator2`.

To pass further arguments to the `configure` method of your configurator, you can use the optional arguments `args` and `kwargs`
in `ConfiguratorPool.add_configurator`.

```python
pool.add_configurator(DummyConfigurator2, kwargs={"environment": "test"})
```

### ApplicationFactory

The `ApplicationFactory` brings all the pieces together and actually executes your configurators.

```python
from flask_appfactoy import ApplicationFactory

factory = ApplicationFactory(pool)
app = factory.create_app(template_folder='my_template_folder')
```

You can also pass any parameters to the create_app function as you would to the `flask.Flask()` constructor.
If no parameters are passed, the flask app is created using `flask.Flask(__name__)`.

Alternatively, if you already have a `flask.Flask` object and only need to configure it using your ConfigurationPool, you can
use the `factory.configure_app(app)` method.

