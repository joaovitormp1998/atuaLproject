from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='produtos/', default='default.jpg')
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class DeliveryRoute(models.Model):
    id = models.AutoField(primary_key=True)  # Campo 'id' personalizado como chave primária
    destination = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    pedido = models.CharField(max_length=100, default="")
    qtd = models.IntegerField(default=1)
    client_phone = models.CharField(max_length=15)
    destination_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    destination_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    def get_delivery_status(self):
        if hasattr(self, 'deliverystatus'):
            return self.deliverystatus.status
        else:
            return 'Pedente'
    def __str__(self):
        return f'Pedido: {self.pedido}'
class DeliveryStatus(models.Model):
    PENDING = 'Pedente'
    DELIVERED = 'Entregue'
    STATUS_CHOICES = [
        (PENDING, 'Pedente'),
        (DELIVERED, 'Entregue'),
    ]
    
    route = models.ForeignKey('DeliveryRoute', on_delete=models.CASCADE, related_name='deliverystatus')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    def __str__(self):
        return f'{self.status} - {self.route}'

    def mark_as_delivered(self):
        self.status = 'Entregue'
        self.save()

    
