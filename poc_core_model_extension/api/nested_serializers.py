"""API nested serializers for poc_core_model_extension."""
from rest_framework import serializers

from nautobot.core.api import WritableNestedSerializer

from poc_core_model_extension import models


class MyModelNestedSerializer(WritableNestedSerializer):
    """MyModel Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:poc_core_model_extension-api:mymodel-detail")

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = "__all__"
