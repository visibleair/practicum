from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('quiz/', include("quizes.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)