"""Tables for poc_core_model_extension."""

import django_tables2 as tables
from nautobot.core.tables import BaseTable, ButtonsColumn, ToggleColumn
from nautobot.dcim.tables.devices import DeviceTable
from nautobot.ipam.tables import IPAddressTable

from poc_core_model_extension import models


class MyModelTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.MyModel,
        pk_field="slug",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.MyModel
        fields = (
            "pk",
            "name",
            "description",
            "devices",
            "ip_addresses",
        )


class DeviceMyModelTable(DeviceTable):
    mymodel = tables.Column(verbose_name="MyModel", accessor="mymodel__first", linkify=True)

    class Meta(DeviceTable.Meta):
        fields = DeviceTable.Meta.fields + ("mymodel",)
        default_columns = DeviceTable.Meta.default_columns + ("mymodel",)


class IPAddressMyModelTable(IPAddressTable):
    mymodel = tables.Column(verbose_name="MyModel", accessor="mymodel__first", linkify=True)

    class Meta(IPAddressTable.Meta):
        fields = IPAddressTable.Meta.fields + ("mymodel",)
        # IPAddress doesn't have a default_columns attribute. All columns are included by default.
        # default_columns = IPAddressTable.Meta.default_columns + ("mymodel",)
