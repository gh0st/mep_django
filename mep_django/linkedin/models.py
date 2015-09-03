from django.db import models
from django.utils.encoding import smart_unicode
from time import time
from django.contrib.auth.models import User
 
# Create your models here.
def get_upload_file_name(instance, filename):
    return "%s_%s" % (str(time()).replace('.','_'), filename)
 
 
class MepUserProfile(models.Model):
    user = models.OneToOneField(User)
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophmore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    def __unicode__(self):
        return smart_unicode(self.user)
 
class V_Event(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.FileField(upload_to=get_upload_file_name)
    def __unicode__(self):
        return smart_unicode(self.title)
 
class Event(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.FileField(upload_to=get_upload_file_name)
    def __unicode__(self):
        return smart_unicode(self.title)
   
class Announcement(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.FileField(upload_to=get_upload_file_name)
    def __unicode__(self):
        return smart_unicode(self.title)
 
class Volunteer(models.Model):
    mep_user = models.ForeignKey(User)
    volunteer_event = models.ForeignKey(V_Event)
    hours = models.IntegerField()
    def  __unicode__(self):
        return smart_unicode(self.hours)
 
class GroupPost(models.Model):
    title = models.CharField(max_length = 500)
    summary = models.TextField()
    creation_timestamp = models.BigIntegerField()
    db_timestamp = models.DateField(auto_now_add = True)
    site_group_post_url = models.URLField()
 
class Manager(models.Model):
    email = models.EmailField()
    def __unicode__(self):
        return smart_unicode(self.email)
   
class CarouselItemModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.FileField(upload_to=get_upload_file_name)
   
    def __unicode__(self):
        return smart_unicode(self.title)