from django.http import JsonResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView  # Importe a DeleteView
from django.views.generic.edit import CreateView
from .models import DeliveryRoute, DeliveryStatus, Product
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from django.shortcuts import redirect,render
from django.shortcuts import get_object_or_404
from .forms import ProductForm  # Certifique-se de criar um formulário para o seu modelo Product


class RouteCreationView(CreateView):
    model = DeliveryRoute
    template_name = "delivery/route_form.html"
    fields = ["pedido", "qtd", "destination", "client_name", "client_phone"]
    # Redirecionar para a mesma página
    success_url = reverse_lazy("create-route")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
    def form_valid(self, form):
        # Chama o método 'form_valid' padrão para salvar o objeto
        response = super().form_valid(form)

        return response
    
class ListarRotasView(ListView):
    model = DeliveryRoute
    # Coordenada de referência (latitude, longitude)
    reference_coord = (-22.48079178754085, -43.50213321102069)

    def get(self, request, *args, **kwargs):
        routes = DeliveryRoute.objects.all()
        route_data = []
        
        for route in routes:
            # Obtém as coordenadas do destino da rota
            destination_coord = (
                route.destination_latitude,
                route.destination_longitude,
            )

            # Calcula a distância entre a coordenada de referência e a coordenada do destino
            distance = self.calculate_distance(
                self.reference_coord, destination_coord)

            route_info = {
                "id": route.id,
                "pedido": route.pedido,
                "qtd": route.qtd,
                "destination": route.destination,
                "client_name": route.client_name,
                "client_phone": route.client_phone,
                "status": self.get_delivery_status(route),
                "distance_to_reference": distance,
            }

            route_data.append(route_info)
        
        data = {"routes": route_data}
        return JsonResponse(data)

    def get_delivery_status(self, route):
        try:
            # Recupere o status mais recente para a rota
            status = route.deliverystatus.latest("id").status
            return status
        except DeliveryStatus.DoesNotExist:
            return "Pendente"

    def calculate_distance(self, coord1, coord2):
        # coord1 e coord2 devem ser tuplas no formato (latitude, longitude)
        return geodesic(coord1, coord2).kilometers
products = Product.objects.all()

class DeleteRouteView(DeleteView):
    model = DeliveryRoute

    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        try:
            route = DeliveryRoute.objects.get(pk=item_id)
            route.delete()
            response_data = {"message": "Item excluído com sucesso"}
        except DeliveryRoute.DoesNotExist:
            response_data = {"message": "Item não encontrado"}

        return JsonResponse(response_data)


class MarkDeliveryView(View):
    def post(self, request, route_id, *args, **kwargs):
        try:
            # Recupere a rota de entrega com base no route_id
            route = DeliveryRoute.objects.get(pk=route_id)

            # Acesse o status através do modelo DeliveryStatus e marque como "Entregue"
            delivery_status, created = DeliveryStatus.objects.get_or_create(
                route=route)
            delivery_status.mark_as_delivered()

            # Responda com uma mensagem de sucesso
            response_data = {
                "success": True,
                "message": "Entrega marcada como concluída",
            }

        except DeliveryRoute.DoesNotExist:
            # Se a rota de entrega não for encontrada, responda com uma mensagem de erro
            response_data = {
                "success": False,
                "message": "Rota de entrega não encontrada",
            }

        return JsonResponse(response_data)


class StockListView(ListView):
    model = Product
    template_name = "stock/stock_list.html"
    context_object_name = "products"
    
def add_product(request):
    if request.method == 'POST':
        # Crie um formulário com os dados do POST e arquivos
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            # Salve o produto com a imagem no banco de dados
            form.save()
            # Redirecione para a página de produtos em estoque
            return redirect('/estoque')
    else:
        form = ProductForm()

    return render(request, 'stock/stock_list.html', {'form': form})
def delete_product(request, product_id):
    # Assuming you have a Product model and you want to delete a product
    product = get_object_or_404(Product, pk=product_id)
    
    # Delete the product
    product.delete()
    return redirect('/estoque')