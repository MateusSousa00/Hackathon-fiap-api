from rest_framework import viewsets
from nossaagua.models import Morador, FaltouAgua
from nossaagua.serializer import MoradorSerializer, FaltouAguaSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os moradores"""
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    
class FaltouAguaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as respostas sobre a água"""
    queryset = FaltouAgua.objects.all()
    serializer_class = FaltouAguaSerializer

