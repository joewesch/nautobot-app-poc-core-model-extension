"""Views for poc_core_model_extension."""

from nautobot.apps.views import NautobotUIViewSet

from poc_core_model_extension import filters, forms, models, tables
from poc_core_model_extension.api import serializers


class MyModelUIViewSet(NautobotUIViewSet):
    """ViewSet for MyModel views."""

    bulk_update_form_class = forms.MyModelBulkEditForm
    filterset_class = filters.MyModelFilterSet
    filterset_form_class = forms.MyModelFilterForm
    form_class = forms.MyModelForm
    lookup_field = "slug"
    queryset = models.MyModel.objects.all()
    serializer_class = serializers.MyModelSerializer
    table_class = tables.MyModelTable
