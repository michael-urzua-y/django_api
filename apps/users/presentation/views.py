from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from apps.users.application.services import UserService
from apps.users.presentation.serializers import UserSerializer

class UserListCreateView(APIView):
    def get(self, request):
        schema = request.GET.get('schema', 'default')
        try:
            service = UserService(schema)
            users = service.list_users()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

    def post(self, request):
        schema = request.GET.get('schema', 'default')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                service = UserService(schema)
                user = service.create_user(**serializer.validated_data)
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist as e:
                return JsonResponse({'error': f'Related object not found: {str(e)}'}, status=400)
            except Exception as e:
                return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, user_id):
        schema = request.GET.get('schema', 'default')
        try:
            service = UserService(schema)
            user = service.get_user(user_id)
            if user:
                serializer = UserSerializer(user)
                return Response(serializer.data)
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

    def put(self, request, user_id):
        schema = request.GET.get('schema', 'default')
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                # Copiamos los datos validados y eliminamos 'user_id' si está presente
                data = serializer.validated_data.copy()
                data.pop('user_id', None)

                service = UserService(schema)
                user = service.update_user(user_id, **data)

                if user:
                    return Response(UserSerializer(user).data)
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            except ObjectDoesNotExist as e:
                return JsonResponse({'error': f'Related object not found: {str(e)}'}, status=400)
            except Exception as e:
                return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        schema = request.GET.get('schema', 'default')
        try:
            service = UserService(schema)
            success = service.delete_user(user_id)
            if success:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
