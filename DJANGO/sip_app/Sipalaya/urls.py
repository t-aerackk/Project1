from django.urls import path
from . import views
from .views import submit_form
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.home,name="Dashboard"),
    path('products/', views.Image_Handler,name="product"),
    path('contact/',views.contact,name="contact" ),
    path('about/',views.about,name="about" ),
    path('', views.home, name='home'),
    path('submit/', submit_form, name='submit_form'),
    path('delete<int:id>', views.DeleteData,name='delete'),
    path('edit/<int:id>', views.EditData,name='edit'),
    path('search/', views.SearchData,name='search'),
    path('eyeglass', views.Eyeglass, name='eye'),
    path('reg/',views.User_Reg,name='reg'),
    path('login/',views.LogIn, name='login'),
    path('logout/', views.HandleLogout,name="logout"),
]