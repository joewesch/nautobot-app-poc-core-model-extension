"""Test MyModel Filter."""
from django.test import TestCase
from poc_core_model_extension import filters
from poc_core_model_extension import models
from poc_core_model_extension.tests import fixtures


class MyModelFilterTestCase(TestCase):
    """MyModel Filter Test Case."""

    queryset = models.MyModel.objects.all()
    filterset = filters.MyModelFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for MyModel Model."""
        fixtures.create_mymodel()

    def test_q_search_name(self):
        """Test using Q search with name of MyModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_search_slug(self):
        """Test using Q search with slug of MyModel."""
        params = {"q": "test-one"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for MyModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
