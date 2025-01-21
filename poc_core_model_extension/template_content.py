from nautobot.apps.ui import TemplateExtension


class DeviceMyModel(TemplateExtension):
    """Template extension to display MyModel on the right side of the page."""

    model = "dcim.device"

    def right_page(self):
        return self.render("poc_core_model_extension/mymodel_extension.html")


class IPAddressMyModel(TemplateExtension):
    """Template extension to display MyModel on the right side of the page."""

    model = "ipam.ipaddress"

    def right_page(self):
        return self.render("poc_core_model_extension/mymodel_extension.html")


class LocationMyModel(TemplateExtension):
    """Template extension to display MyModel on the right side of the page."""

    model = "dcim.location"

    def right_page(self):
        return self.render("poc_core_model_extension/mymodel_extension.html")


template_extensions = [DeviceMyModel, IPAddressMyModel, LocationMyModel]
