
from django.contrib import admin
from django.urls import path

from .views import posts_list

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('post/', posts_list),
]
