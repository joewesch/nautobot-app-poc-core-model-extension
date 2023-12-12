"""Forms for poc_core_model_extension."""
from django import forms

from nautobot.dcim.forms import DeviceForm
from nautobot.dcim.models import Device
from nautobot.extras.forms import CustomFieldModelCSVForm
from nautobot.ipam.models import IPAddress
from nautobot.utilities.forms import (
    BootstrapMixin,
    BulkEditForm,
    SlugField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)

from poc_core_model_extension import models


class CSVMultipleModelChoiceField(forms.ModelMultipleChoiceField):
    """Reference a list of PKs."""

    def prepare_value(self, value):
        """Parse a comma-separated string of PKs into a list of PKs."""
        pk_list = []
        if isinstance(value, str):
            pk_list = [val.strip() for val in value.split(",") if val]

        return super().prepare_value(pk_list)


class CSVIPAddressMultipleModelChoiceField(CSVMultipleModelChoiceField):
    """CSV Multiple Model Choice Field for IP Addresses."""

    def clean(self, value):
        value = self.prepare_value(value)
        return self.queryset.net_in(value)


class MyModelForm(BootstrapMixin, forms.ModelForm):
    """MyModel creation/edit form."""

    slug = SlugField()
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(), required=False, query_params={"poc_core_model_extension_has_mymodel": False}
    )
    address = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
    )

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = [
            "name",
            "slug",
            "description",
            "devices",
            "address",
        ]


class MyModelBulkEditForm(BootstrapMixin, BulkEditForm):
    """MyModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.MyModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class MyModelFilterForm(BootstrapMixin, forms.ModelForm):
    """Filter form to filter searches."""

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
    slug = forms.CharField(required=False, label="Slug")

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
            "name",
            "slug",
            "description",
        ]


class MyModelCSVForm(CustomFieldModelCSVForm):
    """MyModel CSV form."""

    devices = CSVMultipleModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
        to_field_name="name",
        help_text="Comma-separated list of device names",
    )
    address = CSVIPAddressMultipleModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        to_field_name="address",
        help_text="Comma-separated list of IP addresses",
    )

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = models.MyModel.csv_headers


class DeviceMyModelForm(DeviceForm):
    """Sub-class of DeviceForm to add mymodel field."""

    mymodel = DynamicModelChoiceField(queryset=models.MyModel.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["mymodel"] = self.instance.mymodel.first()

    def save(self, *args, **kwargs):
        """Save the form."""
        device = super().save(*args, **kwargs)
        if self.cleaned_data["mymodel"]:
            device.mymodel.set([self.cleaned_data["mymodel"]])
            device.save()
        return device
