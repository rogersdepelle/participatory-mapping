from django.contrib import admin
from django.urls import path

from maps.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('admin/', admin.site.urls),
]
