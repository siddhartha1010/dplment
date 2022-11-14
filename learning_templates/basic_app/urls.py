from django.urls import include, path
from basic_app import views

#TEMPLATE TAGGING

app_name = 'basic_app'


urlpatterns=[
    path('relative',views.relative,name='relative'),
    path('others',views.others,name='other'),
]
