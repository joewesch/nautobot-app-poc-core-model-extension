"""Plugin declaration for poc_core_model_extension."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class POCCoreModelExtensionConfig(PluginConfig):
    """Plugin configuration for the poc_core_model_extension plugin."""

    name = "poc_core_model_extension"
    verbose_name = "POC Core Model Extension"
    version = __version__
    author = "Joe Wesch"
    description = "POC Core Model Extension."
    base_url = "poc-core-model-extension"
    required_settings = []
    min_version = "1.4.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}
    override_views = "views.overrides.override_views"


config = POCCoreModelExtensionConfig  # pylint:disable=invalid-name
