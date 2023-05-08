from nautobot.apps.ui import TemplateExtension


class DeviceMyModel(TemplateExtension):
    """Template extension to display MyModel on the right side of the page."""

    model = "dcim.device"

    def right_page(self):
        return self.render("poc_core_model_extension/device_mymodel.html")


template_extensions = [DeviceMyModel]
