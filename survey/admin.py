from django.contrib import admin
from .models import Question
from .models import Answer
from .models import AnswerTag
from .models import Option

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerTag)
admin.site.register(Option)