from django.conf.urls import url
from suggestions import views
from suggestions.views import validate, SuggestionImagesListAPIView
from suggestions.models import Validation
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^validations/$', views.ValidationList.as_view()),
    url(r'^validations/(?P<pk>[0-9]+)/$', views.ValidationDetail.as_view()),
    url(r'^events/$', views.EventList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventListDetail.as_view()),
    url(r'^suggestions/$', views.SuggestionOptionList.as_view()),
    url(r'^suggestion/images/', views.SuggestionImagesListAPIView.as_view()),
    url(r'^validate/$', views.ValidateView.as_view())


]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
