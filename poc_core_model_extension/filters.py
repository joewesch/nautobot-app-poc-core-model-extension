"""Filtering for poc_core_model_extension."""

from nautobot.utilities.filters import BaseFilterSet, NameSlugSearchFilterSet

from poc_core_model_extension import models


class MyModelFilterSet(BaseFilterSet, NameSlugSearchFilterSet):
    """Filter for MyModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.MyModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "slug", "description"]
