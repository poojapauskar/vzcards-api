"""vzcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('register.urls')),
    url(r'^', include('verify.urls')),
    url(r'^', include('friends.urls')),
  #  url(r'^', include('ticket.urls')),
    url(r'^', include('ticket_create.urls')),
    url(r'^', include('api.urls')),
    url(r'^', include('connect.urls')),
    url(r'^', include('get_list.urls')),
    url(r'^', include('get_my_tickets.urls')),
    url(r'^', include('send_again.urls')),
    url(r'^', include('my_profile.urls')),
    url(r'^', include('response.urls')),
    url(r'^', include('ticket_details.urls')),
    url(r'^', include('sync_contacts.urls')),
    url(r'^', include('get_my_friends.urls')),
    url(r'^', include('sync.urls')),
    url(r'^', include('reffered.urls')),
    url(r'^', include('upload_image.urls')),
    url(r'^', include('history.urls')),
    url(r'^', include('remove_ticket.urls')),
)
