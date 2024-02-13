from django.urls import path
from application.views import *

urlpatterns = [
    path('', index , name='home'),
    path('signin', signin , name='signin'),
    path('logout', logoutuser , name='logoutuser'),
    path('blogs', blogs , name='blogs'),
    path('blog/create/', create_blog, name='create-blog'),
]

