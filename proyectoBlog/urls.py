from django.contrib import admin
from django.urls import path, include
from .views import homepage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('TS/', include("BlogApp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
