from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.users.application.services import UserService

User = get_user_model()

@receiver(post_save, sender=User)
def handle_user_created(sender, instance, created, **kwargs):
    """
    Handler que se ejecuta cuando se crea un nuevo usuario.
    """
    if created:
        print(f"[Handler] Usuario creado: {instance.email}")
        service = UserService()
        service.process_new_user(instance)

@receiver(pre_delete, sender=User)
def handle_user_deleted(sender, instance, **kwargs):
    """
    Handler que se ejecuta antes de eliminar un usuario.
    """
    print(f"[Handler] Usuario eliminado: {instance.email}")
    # Aquí podrías llamar a un servicio para limpiar datos relacionados
