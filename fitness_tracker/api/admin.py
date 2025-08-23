from django.contrib import admin
from .models import Profile, Activity

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height', 'created_at')
    search_fields = ('user__username', 'user__email')
    list_filter = ('created_at',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'distance_km', 'calories_burned', 'date', 'created_at')
    search_fields = ('user__username', 'activity_type')
    list_filter = ('activity_type', 'date', 'created_at')
    ordering = ('-date', '-created_at')
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.    
# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Activity, ActivityAdmin)
# admin.site.register(Profile)
# admin.site.register(Activity)     
