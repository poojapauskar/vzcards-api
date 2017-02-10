from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from vzcard_details import views
#from vzcard_details.views import get_queryset

urlpatterns = [
    url(r'^vzcard_details/$', views.CustomListView.as_view()),
    #url(r'^vzcard_details/$', get_queryset),
    #url(r'^vzcard_details/(?P<vz_id>\d+)/$', views.Vzcard_detailsDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]