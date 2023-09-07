from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='home'),
    path('product/<slug:product_slug>/', views.detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)