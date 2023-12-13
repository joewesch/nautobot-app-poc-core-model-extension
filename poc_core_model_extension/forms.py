"""Forms for poc_core_model_extension."""
from django import forms

from nautobot.core.forms import (
    BootstrapMixin,
    BulkEditForm,
    SlugField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from nautobot.dcim.forms import DeviceForm
from nautobot.dcim.models import Device
from nautobot.ipam.forms import IPAddressForm
from nautobot.ipam.models import IPAddress

from poc_core_model_extension import models


class MyModelForm(BootstrapMixin, forms.ModelForm):
    """MyModel creation/edit form."""

    slug = SlugField()
    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(), required=False, query_params={"poc_core_model_extension_has_mymodel": False}
    )
    ip_addresses = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(), required=False, query_params={"poc_core_model_extension_has_mymodel": False}
    )

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = [
            "name",
            "slug",
            "description",
            "devices",
            "ip_addresses",
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
        else:
            device.mymodel.clear()
        return device


class IPAddressMyModelForm(IPAddressForm):
    """Sub-class of IPAddressForm to add mymodel field."""

    mymodel = DynamicModelChoiceField(queryset=models.MyModel.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["mymodel"] = self.instance.mymodel.first()

    def save(self, *args, **kwargs):
        """Save the form."""
        ip_address = super().save(*args, **kwargs)
        if self.cleaned_data["mymodel"]:
            ip_address.mymodel.set([self.cleaned_data["mymodel"]])
            ip_address.save()
        else:
            ip_address.mymodel.clear()
        return ip_address
