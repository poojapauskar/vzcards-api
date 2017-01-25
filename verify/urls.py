from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from verify import views
from verify.views import get_queryset

urlpatterns = [
    url(r'^verify/$', get_queryset),
    url(r'^verify_list/$', views.VerifyList.as_view()),
    url(r'^verify/(?P<pk>[0-9]+)/$', views.VerifyDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]