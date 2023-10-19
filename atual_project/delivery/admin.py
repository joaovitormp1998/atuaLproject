from django.contrib import admin
from .models import DeliveryRoute, DeliveryStatus, Product


class DeliveryRouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'qtd', 'destination',
                    'client_name', 'client_phone', 'status_display']

    def status_display(self, obj):
        status = 'Pending'
        if hasattr(obj, 'deliverystatus'):
            status = obj.deliverystatus.latest('id').status
        return status

    status_display.short_description = 'Status'


admin.site.register(DeliveryRoute, DeliveryRouteAdmin)


class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display = ['route', 'status']


admin.site.register(DeliveryStatus, DeliveryStatusAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['foto','nome', 'quantidade', 'preco']


admin.site.register(Product, ProductAdmin)
