"""Models for POC Core Model Extension."""

# Django imports
from django.db import models
from django.urls import reverse

# Nautobot imports
from nautobot.core.models import BaseModel
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.utils import extras_features


@extras_features("custom_fields", "custom_validators", "relationships", "graphql")
class MyModel(PrimaryModel):
    """Base model for POC Core Model Extension plugin."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)

    # Only one MyModel can be associated with a Device, but many Devices can be associated to one MyModel.
    # This is a one-to-many relationship.
    devices = models.ManyToManyField(
        "dcim.Device",
        blank=True,
        through="MyModelToDevice",
        related_name="mymodel",
    )

    address = models.ManyToManyField(
        "ipam.IPAddress",
        blank=True,
        related_name="mymodel",
    )

    csv_headers = [
        "name",
        "slug",
        "description",
        "devices",
        "address",
    ]

    class Meta:
        """Meta class."""

        ordering = ["name"]

    def get_absolute_url(self):
        """Return detail view for MyModel."""
        return reverse("plugins:poc_core_model_extension:mymodel", args=[self.slug])

    def __str__(self):
        """Stringify instance."""
        return str(self.name)

    def to_csv(self):
        """Return CSV data for MyModel."""
        return (
            self.name,
            self.slug,
            self.description,
            ",".join(str(device["name"]) for device in self.devices.values()),
            ",".join(f"{address['host']}/{address['prefix_length']}" for address in self.address.values()),
        )


class MyModelToDevice(BaseModel):
    """Through model for tying many MyModels to one Device."""

    mymodel = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    device = models.OneToOneField("dcim.Device", on_delete=models.CASCADE)
