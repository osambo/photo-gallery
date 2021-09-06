from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.photos_of_day,name='photosToday'),
    url(r'^$',views.picture,name = 'picture'),
]