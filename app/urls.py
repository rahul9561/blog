from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='home'),
    path('signup/',signup,name="signup"),
    path('login/',user_login,name="login"),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('edit-blog/<int:id>/',Edit_view,name='edit-blog'),
    path('logout/',logout_view,name='logout'),
    path('create/', create_post, name='create_post'),

]
