from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="survey"
    )


class AnswerTag(models.Model):
    tag = models.CharField(max_length=250)

    def __unicode__(self):
        return self.tag


class Option(models.Model):
    option_description = models.CharField(max_length=250, default="default")
    answer_image = models.FileField()
    answer_tags = models.ManyToManyField(AnswerTag)

    def __unicode__(self):
        return self.option_description


class Question(models.Model):
    text = models.CharField(max_length=250)
    option_1 = models.ForeignKey('Option', related_name="option_1", on_delete=models.CASCADE, blank=True, null=True)
    option_2 = models.ForeignKey('Option', related_name="option_2", on_delete=models.CASCADE, blank=True, null=True)
    option_3 = models.ForeignKey('Option', related_name="option_3", on_delete=models.CASCADE, blank=True, null=True)
    option_4 = models.ForeignKey('Option', related_name="option_4", on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chosen_option = models.IntegerField(choices=((1,1), (2,2), (3,3), (4,4)))

    def __unicode__(self):
        return self.question.text







