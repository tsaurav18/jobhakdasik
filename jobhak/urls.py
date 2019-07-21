from django.contrib import admin
from django.urls import path, include
import jobcomment.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobcomment.views.home, name='home'),
    path('jobcomment/', include('jobcomment.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
