from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import include, path
def home(request):
    return HttpResponse("Welcome to Furniture Shop!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/auth/', include('users.urls')),
    path('api/cart/', include('cart.urls')),
path('api/orders/', include('orders.urls')),
]
path('api/auth/', include('users.urls'))