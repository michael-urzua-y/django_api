from rest_framework import viewsets, status  # Importa herramientas para crear vistas y manejar estados HTTP
from rest_framework.response import Response  # Permite enviar respuestas HTTP
from api.models import Product  # Importa el modelo Product (ORM)
from api.serializers import ProductSerializer  # Importa el serializador para convertir entre objetos y JSON

class ProductViewSet(viewsets.ViewSet):
    """
    Vista personalizada para manejar operaciones CRUD sobre productos.
    """

    def list(self, request):
        # ORM: obtiene todos los productos de la base de datos (SELECT * FROM product)
        products = Product.objects.all()
        # Serializa la lista de productos a formato JSON
        serializer = ProductSerializer(products, many=True)
        # Devuelve la respuesta con los datos serializados
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            # ORM: busca un producto por su clave primaria (SELECT * FROM product WHERE id = pk)
            product = Product.objects.get(pk=pk)
            # Serializa el producto encontrado
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            # Si no se encuentra el producto, devuelve error 404
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        # Crea un serializador con los datos recibidos en el request
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # ORM: guarda el nuevo producto en la base de datos (INSERT INTO product ...)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si los datos no son válidos, devuelve errores de validación
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            # ORM: busca el producto existente por su clave primaria
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Crea un serializador con el producto existente y los nuevos datos
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            # ORM: actualiza el producto en la base de datos (UPDATE product SET ...)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Si los datos no son válidos, devuelve errores de validación
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            # ORM: busca el producto por su clave primaria
            product = Product.objects.get(pk=pk)
            # ORM: elimina el producto de la base de datos (DELETE FROM product WHERE id = pk)
            product.delete()
            return Response({"message": "Producto eliminado"})
        except Product.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
