from django.urls import path
from djangoapp import views

urlpatterns = [
    path('/',views.home,name='Home'),
    path('history/',views.history,name='History'),
    path('leadership/',views.leadership,name='Leadership'),
    path('sites/',views.sites,name='Sites'),

]
