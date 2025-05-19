from django.contrib import admin

# Register your models here.
# myapp/admin.py

from django.contrib.admin.models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_repr', 'action_flag']
    readonly_fields = [f.name for f in LogEntry._meta.fields]

    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

admin.site.register(LogEntry, LogEntryAdmin)

from axes.models import AccessLog, AccessAttempt

class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'attempt_time', 'logout_time')
    readonly_fields = [f.name for f in AccessLog._meta.fields]

    def has_delete_permission(self, request, obj=None): return False
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False

class AccessAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'user_agent')
    readonly_fields = [f.name for f in AccessAttempt._meta.fields]

    def has_delete_permission(self, request, obj=None): return False
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False


admin.site.unregister(AccessAttempt)
admin.site.register(AccessAttempt, AccessAttemptAdmin)

admin.site.unregister(AccessLog)
admin.site.register(AccessLog, AccessLogAdmin)