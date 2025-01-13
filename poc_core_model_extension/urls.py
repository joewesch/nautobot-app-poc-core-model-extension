"""Django urlpatterns declaration for poc_core_model_extension app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from poc_core_model_extension.views import mymodel


router = NautobotUIViewSetRouter()

router.register("mymodel", mymodel.MyModelUIViewSet)


urlpatterns = [
    path(
        "docs/",
        RedirectView.as_view(url=static("poc_core_model_extension/docs/index.html")),
        name="docs",
    ),
]

urlpatterns += router.urls
