from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import dubuggerTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dubuggerTest, name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('', dubuggerTest, name='home'),

    ] + urlpatterns
