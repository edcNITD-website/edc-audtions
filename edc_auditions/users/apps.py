from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "edc_auditions.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import edc_auditions.users.signals  # noqa: F401
        except ImportError:
            pass
