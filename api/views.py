# from rest_framework import viewsets
# from .models import Task, User
# from .serializers import TaskSerializer, UserSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Lista simulada de usuarios
users = [
    {"id": 1, "nombre": "Juan", "email": "juan@example.com"},
    {"id": 2, "nombre": "Ana", "email": "ana@example.com"},
    {"id": 3, "nombre": "Luis", "email": "luis@example.com"},
]

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response(users)

    # GET
    def retrieve(self, request, pk=None):  # 👈 nombre correcto
        user = next((u for u in users if u["id"] == int(pk)), None)
        if user:
            return Response(user)
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # POST
    def create(self, request):
        new_user = request.data
        new_user["id"] = max(u["id"] for u in users) + 1 if users else 1
        users.append(new_user)
        return Response(new_user, status=status.HTTP_201_CREATED)

    # PUT
    def update(self, request, pk=None):
        user = next((u for u in users if u["id"] == int(pk)), None)
        if user:
            user.update(request.data)
            return Response(user)
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE
    def destroy(self, request, pk=None): 
        global users
        users = [u for u in users if u["id"] != int(pk)]
        return Response({"message": "Usuario eliminado"})
