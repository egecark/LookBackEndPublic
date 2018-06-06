from django.conf.urls import url
from survey import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^questions/$', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionList.as_view()),
    url(r'^options/$', views.OptionList.as_view()),
    url(r'^options/(?P<pk>[0-9]+)/$', views.OptionList.as_view()),
    url(r'^answers/$', views.AnswerList.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])