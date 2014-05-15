from django.contrib import admin
from .models import *
 
# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    class Meta:
        model = Manager
       
class V_EventAdmin(admin.ModelAdmin):
    class Meta:
        model = V_Event
       
class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event
 
class AnnouncementAdmin(admin.ModelAdmin):
    class Meta:
        model = Announcement
 
class VolunteerAdmin(admin.ModelAdmin):
    class Meta:
        model = Volunteer
       
class GroupPostAdmin(admin.ModelAdmin):
    class Meta:
        model = GroupPost
       
class MepUserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = MepUserProfile
       
 
admin.site.register(Manager, ManagerAdmin)
admin.site.register(V_Event, V_EventAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(GroupPost, GroupPostAdmin)
admin.site.register(MepUserProfile, MepUserProfileAdmin)