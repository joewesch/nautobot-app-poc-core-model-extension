"""Views for MyModel."""

from nautobot.core.views import generic

from poc_core_model_extension import filters, forms, models, tables


class MyModelListView(generic.ObjectListView):
    """List view."""

    queryset = models.MyModel.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.MyModelFilterSet
    filterset_form = forms.MyModelFilterForm
    table = tables.MyModelTable

    # Option for modifying the top right buttons on the list view:
    # action_buttons = ("add", "import", "export")


class MyModelView(generic.ObjectView):
    """Detail view."""

    queryset = models.MyModel.objects.all()


class MyModelCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.MyModel
    queryset = models.MyModel.objects.all()
    model_form = forms.MyModelForm


class MyModelDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.MyModel
    queryset = models.MyModel.objects.all()


class MyModelEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.MyModel
    queryset = models.MyModel.objects.all()
    model_form = forms.MyModelForm


class MyModelBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more MyModel records."""

    queryset = models.MyModel.objects.all()
    table = tables.MyModelTable


class MyModelBulkEditView(generic.BulkEditView):
    """View for editing one or more MyModel records."""

    queryset = models.MyModel.objects.all()
    table = tables.MyModelTable
    form = forms.MyModelBulkEditForm


class MyModelBulkImportView(generic.BulkImportView):
    """View for importing one or more MyModel records."""

    queryset = models.MyModel.objects.all()
    model_form = forms.MyModelCSVForm
    table = tables.MyModelTable
    default_return_url = "plugins:poc_core_model_extension:mymodel_list"
