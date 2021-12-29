from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogadmin),
    path('adminboard/',views.adminboard),
    path('category/',views.category),
    path('adminpd/',views.adminpassword),

]