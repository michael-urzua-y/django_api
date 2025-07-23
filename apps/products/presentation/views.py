from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.products.presentation.serializers import ProductSerializer
from apps.products.application import services

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = services.get_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = services.get_product(pk)
        if not product:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = services.create_new_product(serializer.validated_data)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = services.update_existing_product(pk, serializer.validated_data)
            if not product:
                return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        success = services.delete_existing_product(pk)
        if not success:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Producto eliminado"})
