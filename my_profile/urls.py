from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from my_profile import views

urlpatterns = [
    url(r'^my_profile/$', views.My_profileList.as_view()),
    url(r'^my_profile/(?P<vz_id>[A-Z0-9]+)/$', views.My_profileDetail.as_view()),
    url(r'^my_profile/update/(?P<vz_id>(\w+))/(?P<firstname>(\w+))/(?P<lastname>(\w+))/(?P<email>(\w+))/(?P<industry>(\w+))/(?P<address_line_1>(\w+))/(?P<address_line_2>(\w+))/(?P<city>(\w+))/(?P<pin_code>(\w+))/$', views.My_profileUpdate.as_view()),
    #url(r'^get_list/(?P<vz_id>\d+)/$', views.Get_listDetail.as_view(), name='urlname'),

    
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]