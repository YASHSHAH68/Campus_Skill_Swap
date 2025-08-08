from django.apps import AppConfig


class SkillSessionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.skill_sessions"
    
    def ready(self):
        import apps.skill_sessions.signals
