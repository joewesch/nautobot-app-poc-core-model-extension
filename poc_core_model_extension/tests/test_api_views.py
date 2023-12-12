"""Unit tests for poc_core_model_extension."""
from nautobot.core.testing import APIViewTestCases

from poc_core_model_extension import models
from poc_core_model_extension.tests import fixtures


class MyModelAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for MyModel."""

    model = models.MyModel
    create_data = [
        {
            "name": "Test Model 1",
            "slug": "test-model-1",
        },
        {
            "name": "Test Model 2",
            "slug": "test-model-2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}
    brief_fields = ["created", "description", "display", "id", "last_updated", "name", "slug", "url"]

    @classmethod
    def setUpTestData(cls):
        fixtures.create_mymodel()
