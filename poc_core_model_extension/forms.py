"""Forms for poc_core_model_extension."""
from django import forms

from nautobot.dcim.forms import DeviceForm
from nautobot.dcim.models import Device
from nautobot.utilities.forms import (
    BootstrapMixin,
    BulkEditForm,
    SlugField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)

from poc_core_model_extension import models


class MyModelForm(BootstrapMixin, forms.ModelForm):
    """MyModel creation/edit form."""

    slug = SlugField()
    devices = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False)

    class Meta:
        """Meta attributes."""

        model = models.MyModel
        fields = [
            "name",
            "slug",
            "description",
            "devices",
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
        return device
