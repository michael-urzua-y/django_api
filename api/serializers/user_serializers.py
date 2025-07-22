from rest_framework import serializers
from api.models import User

class DireccionSerializer(serializers.Serializer):
    calle = serializers.CharField()
    comuna = serializers.CharField()
    pais = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer(write_only=True)
    salida_direccion = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'nombre', 'email', 'direccion', 'salida_direccion']

    def get_salida_direccion(self, obj):
        return {
            "calle": obj.direccion,
            "comuna": obj.comuna,
            "pais": obj.pais
        }

    def create(self, validated_data):
        direccion_data = validated_data.pop('direccion')
        validated_data['direccion'] = direccion_data['calle']
        validated_data['comuna'] = direccion_data['comuna']
        validated_data['pais'] = direccion_data['pais']
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        direccion_data = validated_data.pop('direccion', None)
        if direccion_data:
            instance.direccion = direccion_data.get('calle', instance.direccion)
            instance.comuna = direccion_data.get('comuna', instance.comuna)
            instance.pais = direccion_data.get('pais', instance.pais)

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
