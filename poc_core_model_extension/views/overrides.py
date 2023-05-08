"""Views for MyModel."""
from nautobot.dcim.views import DeviceEditView, DeviceListView

from poc_core_model_extension.forms import DeviceMyModelForm
from poc_core_model_extension.tables import DeviceMyModelTable


class DeviceMyModelEditView(DeviceEditView):
    """Sub-class of DeviceEditView to override the form used for editing devices."""

    model_form = DeviceMyModelForm
    template_name = "poc_core_model_extension/device_edit_override.html"


class DeviceMyModelListView(DeviceListView):
    table = DeviceMyModelTable


override_views = {
    "dcim:device_add": DeviceMyModelEditView.as_view(),
    "dcim:device_edit": DeviceMyModelEditView.as_view(),
    "dcim:device_list": DeviceMyModelListView.as_view(),
}
