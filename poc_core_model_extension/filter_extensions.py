"""Filter extensions for poc_core_model_extension plugin."""

from nautobot.apps.filters import (
    FilterExtension,
    RelatedMembershipBooleanFilter,
    NaturalKeyOrPKMultipleChoiceFilter,
)
from nautobot.apps.forms import DynamicModelMultipleChoiceField

from poc_core_model_extension.models import MyModel


class DeviceFilterExtension(FilterExtension):
    """Adding filters to Device."""

    model = "dcim.device"

    filterset_fields = {
        "poc_core_model_extension_mymodel": NaturalKeyOrPKMultipleChoiceFilter(
            field_name="mymodel",
            to_field_name="name",
            queryset=MyModel.objects.all(),
            label="MyModel",
        ),
        "poc_core_model_extension_has_mymodel": RelatedMembershipBooleanFilter(
            field_name="mymodel", label="Has MyModel Associated"
        ),
    }

    filterform_fields = {
        "poc_core_model_extension_mymodel": DynamicModelMultipleChoiceField(
            queryset=MyModel.objects.all(),
            required=False,
            to_field_name="name",
            label="MyModel Search",
        ),
    }


class IPAddressFilterExtension(FilterExtension):
    """Adding filters to IPAddress."""

    model = "ipam.ipaddress"

    filterset_fields = {
        "poc_core_model_extension_mymodel": NaturalKeyOrPKMultipleChoiceFilter(
            field_name="mymodel",
            to_field_name="name",
            queryset=MyModel.objects.all(),
            label="MyModel",
        ),
        "poc_core_model_extension_has_mymodel": RelatedMembershipBooleanFilter(
            field_name="mymodel", label="Has MyModel Associated"
        ),
    }

    filterform_fields = {
        "poc_core_model_extension_mymodel": DynamicModelMultipleChoiceField(
            queryset=MyModel.objects.all(),
            required=False,
            to_field_name="name",
            label="MyModel Search",
        ),
    }


filter_extensions = [DeviceFilterExtension, IPAddressFilterExtension]
