"""Create fixtures for tests."""
from poc_core_model_extension.models import MyModel


def create_mymodel():
    """Fixture to create necessary number of MyModel for tests."""
    MyModel.objects.create(name="Test One", slug="test-one")
    MyModel.objects.create(name="Test Two", slug="test-two")
    MyModel.objects.create(name="Test Three", slug="test-three")
