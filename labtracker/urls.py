from django.contrib import admin
from django.urls import path , include
from labtracker import views
from allauth.account.views import  LoginView
from django.views.generic.base import TemplateView
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(),name='home'),
    path('index/',views.index,name='index'),
    path('accounts/login/index/',views.index,name='index'),
    path('accounts/signup/index/',views.index,name='index'),
    path('search_lab/',views.serach_view,name='search_lab'),
    path('search_lab_list/',views.searc_lab_list,name='search_lab_list'),

    
]

urlpatterns += [
    
    path('second/', TemplateView.as_view(template_name='labtracker/second.html'), name ='second'),
    path('search_near_lab/', views.search_near_lab, name='search_near_lab')
]
