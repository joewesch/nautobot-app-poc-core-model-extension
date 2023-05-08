"""Django API urlpatterns declaration for poc_core_model_extension plugin."""

from nautobot.core.api import OrderedDefaultRouter

from poc_core_model_extension.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("mymodel", views.MyModelViewSet)


app_name = "poc_core_model_extension-api"
urlpatterns = router.urls
