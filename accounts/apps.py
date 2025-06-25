from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
#  this ready function is ressponisble for connecting the signal for our model because we create  a new file for that.
    def ready(self):
        import accounts.signals
