from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/scheme", SpectacularAPIView.as_view(), name='api_schema'),
    path("api/docs", SpectacularSwaggerView.as_view(url_name='api_schema'), name='api_docs')
]
