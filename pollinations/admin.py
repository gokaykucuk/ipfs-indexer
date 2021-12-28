from django.contrib import admin

# Register your models here.
from pollinations.models import Task, Content
from djangoql.admin import DjangoQLSearchMixin


@admin.register(Task)
class TaskAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ["id", "cid", "state_updates"]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Content)
class ContentAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ["id", "text_input", "output_video_tag"]

    def has_delete_permission(self, request, obj=None):
        return False
