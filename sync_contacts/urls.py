from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from sync_contacts import views

urlpatterns = [
    url(r'^sync_contacts/$', views.Sync_contactsList.as_view()),
    url(r'^sync_contacts/(?P<pk>[0-9]+)/$', views.Sync_contactsDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]