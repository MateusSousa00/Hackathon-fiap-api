from rest_framework import serializers
from nossaagua.models import Morador, FaltouAgua

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = ['id', 'cpf', 'email', 'celular', 'rua', 'numero_casa', 'bairro', 'cep']
        
class FaltouAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaltouAgua
        fields = '__all__'