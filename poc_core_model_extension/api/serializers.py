"""API serializers for poc_core_model_extension."""
from rest_framework import serializers

from nautobot.core.api import SerializedPKRelatedField
from nautobot.core.api.serializers import ValidatedModelSerializer
from nautobot.dcim.api.nested_serializers import NestedDeviceSerializer
from nautobot.dcim.models import Device
from nautobot.ipam.api.nested_serializers import NestedIPAddressSerializer
from nautobot.ipam.models import IPAddress

from poc_core_model_extension import models

from . import nested_serializers  # noqa: F401, pylint: disable=unused-import


class MyModelSerializer(ValidatedModelSerializer):
    """MyModel Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:poc_core_model_extension-api:mymodel-detail")
    devices = SerializedPKRelatedField(
        queryset=Device.objects.all(),
        serializer=NestedDeviceSerializer,
        required=False,
        many=True,
    )
    address = SerializedPKRelatedField(
        queryset=IPAddress.objects.all(),
        serializer=NestedIPAddressSerializer,
        required=False,
        many=True,
    )

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
