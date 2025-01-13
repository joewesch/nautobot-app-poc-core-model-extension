"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:poc_core_model_extension:mymodel_list",
        name="MyModel",
        permissions=["poc_core_model_extension.view_mymodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:poc_core_model_extension:mymodel_add",
                permissions=["poc_core_model_extension.add_mymodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Devices",
        groups=(NavMenuGroup(name="MyModel", items=tuple(items)),),
    ),
)
