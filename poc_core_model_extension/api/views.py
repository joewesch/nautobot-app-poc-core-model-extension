"""API views for poc_core_model_extension."""

from nautobot.core.api.views import ModelViewSet

from poc_core_model_extension import filters, models

from poc_core_model_extension.api import serializers


class MyModelViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """MyModel viewset."""

    queryset = models.MyModel.objects.all()
    serializer_class = serializers.MyModelSerializer
    filterset_class = filters.MyModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
