from django.contrib import admin
from django.urls import path, include
from delivery.views import RouteCreationView, ListarRotasView, DeleteRouteView, MarkDeliveryView, StockListView
from delivery.views import add_product, delete_product
from django.conf import settings
from django.conf.urls.static import static

# Defina urlpatterns como uma lista vazia
urlpatterns = []

# Adicione suas rotas à lista urlpatterns
urlpatterns += [
    path('', RouteCreationView.as_view(), name='create-route'),
    path('listar/', ListarRotasView.as_view(), name='listar-route'),
    path('delete/<int:pk>/', DeleteRouteView.as_view(), name='delete-route'),
    path('mark_delivered/<int:route_id>/', MarkDeliveryView.as_view(), name='mark_delivered'),
    path('estoque/', StockListView.as_view(), name='stock-list'),
    path('add-product/', add_product, name='add-product'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('admin/', admin.site.urls),
]

# Adicione a configuração para servir arquivos de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
