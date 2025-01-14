"""App declaration for poc_core_model_extension."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class POCCoreModelExtensionConfig(NautobotAppConfig):
    """App configuration for the poc_core_model_extension app."""

    name = "poc_core_model_extension"
    verbose_name = "POC Core Model Extension"
    version = __version__
    author = "Joe Wesch"
    description = "POC Core Model Extension."
    base_url = "poc-core-model-extension"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    override_views = "views.overrides.override_views"


config = POCCoreModelExtensionConfig  # pylint:disable=invalid-name
