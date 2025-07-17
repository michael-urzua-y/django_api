from rest_framework import viewsets, status
from rest_framework.response import Response

# Lista simulada de productos
products = [
    {"id": 1, "name": "Silla", "description": "Silla ergonómica", "price": 49.99, "stock": 10},
    {"id": 2, "name": "Mesa", "description": "Mesa de comedor", "price": 89.99, "stock": 5},
]

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response(products)

    def retrieve(self, request, pk=None):
        product = next((p for p in products if p["id"] == int(pk)), None)
        if product:
            return Response(product)
        return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        new_product = request.data
        new_product["id"] = max(p["id"] for p in products) + 1 if products else 1
        products.append(new_product)
        return Response(new_product, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        product = next((p for p in products if p["id"] == int(pk)), None)
        if product:
            product.update(request.data)
            return Response(product)
        return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        global products
        products = [p for p in products if p["id"] != int(pk)]
        return Response({"message": "Producto eliminado"})
