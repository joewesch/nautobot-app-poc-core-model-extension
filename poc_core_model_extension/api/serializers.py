"""API serializers for poc_core_model_extension."""
from rest_framework import serializers

from nautobot.core.api.serializers import ValidatedModelSerializer

from poc_core_model_extension import models

from . import nested_serializers  # noqa: F401, pylint: disable=unused-import


class MyModelSerializer(ValidatedModelSerializer):
    """MyModel Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:poc_core_model_extension-api:mymodel-detail")

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
