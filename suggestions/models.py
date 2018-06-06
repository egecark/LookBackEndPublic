from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import  settings
import os
"""
Notes:
+ Eger explicitly yeni primary key vermezsen django otomatik "id" fieldi ekler
+ Related field'larda (foreign key) sadece child'a atribute olarak parent eklenir.
other way around degil.
+ Fieldlar birer class parantez koyup obje olarak init etmen lazim
+ Eger usera cilgin bi ozellik katmiycaksan djnagonun kendi userini kullan

"""


class EventTag(models.Model):
    tag_name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.tag_name


from uuid import uuid4
def x(): return str(uuid4())
class EventType(models.Model):
    name = models.CharField(max_length=250)
    code_name= models.CharField(max_length=250, default=x, unique=True)
    tags = models.ManyToManyField(EventTag)

    def __unicode__(self):
        return self.name


class Validation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.BooleanField(help_text="Helpful?")
    outfit_image = models.FileField(max_length=700, blank=True, null=True)
    event_type = models.ForeignKey(EventType)
    event_date = models.DateTimeField(max_length=250)

    def image_path(self):
        return os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, self.outfit_image.name)

    def __unicode__(self):
        return self.event_type.name


class ImageTag(models.Model):
    tag = models.CharField(max_length=250)

    def __unicode__(self):
        return self.tag


class SuggestionOption(models.Model):
    answer_image = models.FileField(max_length=700, blank=True, null=True)
    event_type = models.ForeignKey(EventType,on_delete=models.CASCADE)
    image_tags = models.ManyToManyField(ImageTag)

    def __unicode__(self):
        return self.event_type.name


class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option_1 = models.ForeignKey('SuggestionOption', related_name="option_1", on_delete=models.CASCADE, blank=True, null=True)
    option_2 = models.ForeignKey('SuggestionOption', related_name="option_2", on_delete=models.CASCADE, blank=True, null=True)
    option_3 = models.ForeignKey('SuggestionOption', related_name="option_3", on_delete=models.CASCADE, blank=True, null=True)
    option_4 = models.ForeignKey('SuggestionOption', related_name="option_4", on_delete=models.CASCADE, blank=True, null=True)
    option_5 = models.ForeignKey('SuggestionOption', related_name="option_5", on_delete=models.CASCADE, blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    feedback = models.IntegerField(blank=True, null=True)


class SuggestionImages(models.Model):
    event_type = models.ForeignKey(EventType)
    image = models.FileField(max_length=700, blank=True, null=True, upload_to="media")





