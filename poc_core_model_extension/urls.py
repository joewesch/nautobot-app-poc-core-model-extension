"""Django urlpatterns declaration for poc_core_model_extension plugin."""
from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from poc_core_model_extension import models
from poc_core_model_extension.views import mymodel

urlpatterns = [
    # MyModel URLs
    path("mymodel/", mymodel.MyModelListView.as_view(), name="mymodel_list"),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path("mymodel/add/", mymodel.MyModelCreateView.as_view(), name="mymodel_add"),
    path("mymodel/delete/", mymodel.MyModelBulkDeleteView.as_view(), name="mymodel_bulk_delete"),
    path("mymodel/edit/", mymodel.MyModelBulkEditView.as_view(), name="mymodel_bulk_edit"),
    path("mymodel/<slug:slug>/", mymodel.MyModelView.as_view(), name="mymodel"),
    path("mymodel/<slug:slug>/delete/", mymodel.MyModelDeleteView.as_view(), name="mymodel_delete"),
    path("mymodel/<slug:slug>/edit/", mymodel.MyModelEditView.as_view(), name="mymodel_edit"),
    path(
        "mymodel/<slug:slug>/changelog/",
        ObjectChangeLogView.as_view(),
        name="mymodel_changelog",
        kwargs={"model": models.MyModel},
    ),
]
