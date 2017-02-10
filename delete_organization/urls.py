from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from delete_organization import views

urlpatterns = [
    url(r'^delete_organization/$', views.Delete_organizationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)