"""API serializers for poc_core_model_extension."""
from rest_framework import serializers

from nautobot.core.api.fields import SerializedPKRelatedField
from nautobot.core.api.serializers import ValidatedModelSerializer, BaseModelSerializer
from nautobot.core.utils.data import is_uuid
from nautobot.dcim.api.serializers import DeviceSerializer
from nautobot.dcim.models import Device
from nautobot.ipam.api.serializers import IPAddressSerializer
from nautobot.ipam.models import IPAddress

from poc_core_model_extension import models


class M2MRelatedField(SerializedPKRelatedField):
    """Many to Many related field."""

    def to_internal_value(self, data):
        """To internal value method for DeviceField.

        This method accepts a UUID, a name, or a dictionary of attributes.
        """
        queryset = self.get_queryset()
        if is_uuid(data):
            return queryset.get(pk=data)
        if isinstance(data, str):
            return queryset.get(name=data)
        if isinstance(data, dict):
            return queryset.get(**data)
        raise serializers.ValidationError("Invalid device: {}".format(data))


class DeviceRelatedField(M2MRelatedField):
    def to_representation(self, value):
        return {"id": value.pk, "name": value.name, "url": value.get_absolute_url()}


class IPAddressRelatedField(M2MRelatedField):
    def to_representation(self, value):
        return {"id": value.pk, "address": value.address, "url": value.get_absolute_url()}


class DeviceModelSerializerMixin(BaseModelSerializer):
    """Mixin to enable a writable M2M Device field."""

    devices = DeviceRelatedField(many=True, queryset=Device.objects.all(), serializer=DeviceSerializer)
    ip_addresses = IPAddressRelatedField(many=True, queryset=IPAddress.objects.all(), serializer=IPAddressSerializer)

    def get_field_names(self, declared_fields, info):
        """Get field names for MyModelSerializer."""
        fields = super().get_field_names(declared_fields, info)
        if not self.is_nested:
            self.extend_field_names(fields, "devices")
            self.extend_field_names(fields, "ip_addresses")
        return fields

    def create(self, validated_data):
        """Create method for MyModelSerializer."""
        devices = validated_data.pop("devices", None)
        ip_addresses = validated_data.pop("ip_addresses", None)
        instance = super().create(validated_data)

        if devices is not None:
            return self._save_devices(instance, devices)
        if ip_addresses is not None:
            return self._save_ip_addresses(instance, ip_addresses)

        return instance

    def update(self, instance, validated_data):
        """Update method for MyModelSerializer."""
        devices = validated_data.pop("devices", None)
        ip_addresses = validated_data.pop("ip_addresses", None)

        instance = super().update(instance, validated_data)

        if devices is not None:
            return self._save_devices(instance, devices)

        if ip_addresses is not None:
            return self._save_ip_addresses(instance, ip_addresses)

        return instance

    def _save_devices(self, instance, devices):
        if devices:
            instance.devices.set(devices)
        else:
            instance.devices.clear()

        return instance

    def _save_ip_addresses(self, instance, ip_addresses):
        if ip_addresses:
            instance.ip_addresses.set(ip_addresses)
        else:
            instance.ip_addresses.clear()

        return instance

    def to_representation(self, instance):
        """Representation method for MyModelSerializer."""
        data = super().to_representation(instance)
        if self._is_csv_request():
            if data.get("devices"):
                # Export device names for CSV
                data["devices"] = list(instance.devices.values_list("name", flat=True))
            if data.get("ip_addresses"):
                # Export ip_address addresses for CSV
                data["ip_addresses"] = list(instance.ip_addresses.values_list("address", flat=True))
        return data


class MyModelSerializer(DeviceModelSerializerMixin, ValidatedModelSerializer):
    """MyModel Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:poc_core_model_extension-api:mymodel-detail")

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
