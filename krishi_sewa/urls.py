from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "Krishi Sewa Admin"
admin.site.site_title = "Krishi Sewa Admin Portal"
admin.site.index_title = "Welcome to Krishi Sewa Administration Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls'))
]