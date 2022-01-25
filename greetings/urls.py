from django.contrib import admin
from django.urls import include, path
from .views import PersonCreate, PersonList
urlpatterns = [
    path('check/', PersonCreate.as_view(), name='person_check_url'),
    path('list/', PersonList.as_view(), name='person_list_url'),
    # path('check/', index, name='yes_url'),
    # path('yes/', PersonList.as_view(), name='yes_url')
]