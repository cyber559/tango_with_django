<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from django.urls import include
=======
from django.urls import path
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
=======
>>>>>>> 8a1a396d807343e892f49a2fa7a604835b8f60d5
]