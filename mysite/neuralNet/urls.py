from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^$', views.neuralNetImagePredict, name='index'),
     url(r'^(?P<num1>\d+)/(?P<num2>\d+)/$', views.neuralNetAddition),
]