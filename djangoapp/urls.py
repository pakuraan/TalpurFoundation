from django.urls import path
from djangoapp import views

urlpatterns = [
    path('home/',views.index,name='index'),
    path('history/',views.history,name='History'),
    path('leadership/',views.leadership,name='Leadership'),
    path('sites/',views.sites,name='Sites'),

]
