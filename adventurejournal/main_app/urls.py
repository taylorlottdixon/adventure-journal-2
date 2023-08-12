from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('campaigns/', views.campaigns_index, name='campaigns_index'),
    path('accounts/signup/', views.signup, name='signup'),
]