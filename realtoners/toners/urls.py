from django.urls import include, path
from toners import views


urlpatterns = [
    path('', views.index, name='index'),

]