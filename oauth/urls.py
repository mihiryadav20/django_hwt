from django.urls import path, include
from django.contrib import admin
from theapp.views import UserList, UserDetails, GroupList
from oauth2_provider import urls as oauth2_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(oauth2_urls)),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<pk>/', UserDetails.as_view(), name='user-details'),
    path('groups/', GroupList.as_view(), name='group-list'),
]
