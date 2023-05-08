"""Test MyModel."""

from django.test import TestCase

from poc_core_model_extension import models


class TestMyModel(TestCase):
    """Test MyModel."""

    def test_create_mymodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        mymodel = models.MyModel.objects.create(name="Development", slug="development")
        self.assertEqual(mymodel.name, "Development")
        self.assertEqual(mymodel.description, "")
        self.assertEqual(str(mymodel), "Development")
        self.assertEqual(mymodel.slug, "development")

    def test_create_mymodel_all_fields_success(self):
        """Create MyModel with all fields."""
        mymodel = models.MyModel.objects.create(
            name="Development", slug="development", description="Development Test"
        )
        self.assertEqual(mymodel.name, "Development")
        self.assertEqual(mymodel.slug, "development")
        self.assertEqual(mymodel.description, "Development Test")
