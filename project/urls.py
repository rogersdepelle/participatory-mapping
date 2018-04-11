from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from maps.views import ParticipatoryMapsListView, ParticipatoryMapDetailView


urlpatterns = [
    path('', ParticipatoryMapsListView.as_view(), name='pmap_list_view'),
    path('mapa/<int:pk>/', ParticipatoryMapDetailView.as_view(), name='pmap_detail_view'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
