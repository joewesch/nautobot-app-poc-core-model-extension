"""Menu items."""

from nautobot.apps.ui import NavMenuItem, NavMenuAddButton, NavMenuTab, NavMenuGroup

menu_items = (
    NavMenuTab(
        name="POC Core Model Extension",
        weight=100,
        groups=(
            NavMenuGroup(
                name="MyModel",
                weight=100,
                items=(
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
                ),
            ),
        ),
    ),
)
