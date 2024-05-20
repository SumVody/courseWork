from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'

urlpatterns = [
    path('', views.sites.index, name='home'),
    path('about/', views.sites.about, name='about'),
    path('cars/', views.sites.cars, name='cars'),
    path('profile/', views.sites.profile, name='profile'),
    path('registration/', views.sites.register, name='registration'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('rent/<int:id>/', views.sites.rent_car, name='rent_car'),
    path('end/<int:rental_id>/', views.sites.end_rental, name='end_rental'),
    path('pay/<int:rental_id>/', views.sites.pay_rental, name='pay_rental'),
]
