"""Views for MyModel."""
from django.shortcuts import render

from nautobot.dcim.views import DeviceEditView, DeviceListView
from nautobot.ipam.views import PrefixEditView, IPAddressEditView, IPAddressListView

from poc_core_model_extension.forms import DeviceMyModelForm, IPAddressMyModelForm
from poc_core_model_extension.tables import DeviceMyModelTable, IPAddressMyModelTable


class DeviceMyModelEditView(DeviceEditView):
    """Sub-class of DeviceEditView to override the form used for editing devices."""

    model_form = DeviceMyModelForm
    template_name = "poc_core_model_extension/device_edit_override.html"


class DeviceMyModelListView(DeviceListView):
    table = DeviceMyModelTable


class IPAddressMyModelEditView(IPAddressEditView):
    """Sub-class of IPAddressEditView to override the form used for editing IP addresses."""

    model_form = IPAddressMyModelForm
    template_name = "poc_core_model_extension/ipaddress_edit_override.html"


class IPAddressMyModelListView(IPAddressListView):
    table = IPAddressMyModelTable


class DisablePrefixStatusOverrideView(PrefixEditView):
    def post(self, request, *args, **kwargs):
        """Override post method to limit the ability to change the Status to a specific Group."""
        obj = self.get_object(kwargs)
        form = self.model_form(data=request.POST, files=request.FILES, instance=obj)
        # Only process the custom validation if the form is otherwise valid
        if form.is_valid() and request.user.groups.filter(name="Disable Status").exists():
            current_obj = self.queryset.get(pk=obj.pk)
            current_status = current_obj.status
            new_status = form.cleaned_data["status"]
            if current_status != new_status:
                form.add_error(
                    "status",
                    f"You don't have permission to change Status from {current_status} to {new_status}.",
                )
                return render(
                    request,
                    self.template_name,
                    {
                        "obj": obj,
                        "obj_type": self.queryset.model._meta.verbose_name,
                        "form": form,
                        "return_url": self.get_return_url(request, obj),
                        "editing": obj.present_in_database,
                        **self.get_extra_context(request, obj),
                    },
                )
        return super().post(request, *args, **kwargs)


override_views = {
    "dcim:device_add": DeviceMyModelEditView.as_view(),
    "dcim:device_edit": DeviceMyModelEditView.as_view(),
    "dcim:device_list": DeviceMyModelListView.as_view(),
    "ipam:prefix_edit": DisablePrefixStatusOverrideView.as_view(),
    "ipam:ipaddress_add": IPAddressMyModelEditView.as_view(),
    "ipam:ipaddress_edit": IPAddressMyModelEditView.as_view(),
    "ipam:ipaddress_list": IPAddressMyModelListView.as_view(),
}
