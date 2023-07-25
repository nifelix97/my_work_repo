from django.contrib import admin
from django.urls import path
from speakers import views
from .views import home,event_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('event_list/', views.event_list, name='event_list'),
    # path('event', views.event, name= 'event'),

]