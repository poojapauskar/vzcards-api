from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from check_is_organization import views
from check_is_organization.views import get_queryset


urlpatterns = [
    url(r'^check_is_organization/$', get_queryset),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]