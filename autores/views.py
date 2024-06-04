from rest_framework import generics
from autores.models import Autor
from autores.serializers import AutorSerializer


class AutorCreateListView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
