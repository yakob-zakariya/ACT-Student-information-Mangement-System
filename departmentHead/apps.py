from django.apps import AppConfig


class DepartmentHeadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'departmentHead'
    
    def ready(self):
        import departmentHead.signals
