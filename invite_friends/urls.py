from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from invite_friends import views
#from history.views import get_queryset

urlpatterns = [
	url(r'^invite_friends/$', views.CustomListView.as_view()),
    #url(r'^my_profile/$', views.My_profileList.as_view()),
    #url(r'^history/$', get_queryset),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]