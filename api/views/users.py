from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import User
from api.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):

    
    def list(self, request):
        print("LLEGUE")
        users = User.objects.all()  # ORM: obtiene todos los usuarios de la base de datos
        serializer = UserSerializer(users, many=True)  # Serializa la lista de usuarios
        return Response(serializer.data)  # Devuelve los datos en formato JSON



    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)  # ORM: busca un usuario por su clave primaria
            serializer = UserSerializer(user)  # Serializa el objeto usuario
            return Response(serializer.data)  # Devuelve los datos en formato JSON
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)


    def create(self, request):
        serializer = UserSerializer(data=request.data)  # Crea el serializador con los datos recibidos
        if serializer.is_valid():  # Valida los datos
            serializer.save()  # ORM: crea un nuevo registro en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        try:
            # Consulta ORM para obtener el usuario por su clave primaria
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            # Si no se encuentra, se devuelve un error 404
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Se instancia el serializador con el objeto existente y los nuevos datos
        serializer = UserSerializer(user, data=request.data)

        # Validación de los datos
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Guardado de los datos actualizados en la base de datos (ORM en acción)
        serializer.save()

        # Respuesta con los datos actualizados
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)  # ORM: busca el usuario por su clave primaria
            user.delete()  # ORM: elimina el objeto de la base de datos (DELETE)
            return Response({"message": "Usuario eliminado"})  # Respuesta exitosa
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

