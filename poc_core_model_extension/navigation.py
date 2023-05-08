"""Menu items."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:poc_core_model_extension:mymodel_list",
        link_text="POC Core Model Extension",
        permissions=["poc_core_model_extension.view_mymodel"],
        buttons=(
            PluginMenuButton(
                link="plugins:poc_core_model_extension:mymodel_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["poc_core_model_extension.add_mymodel"],
            ),
        ),
    ),
)
