from rest_framework import viewsets
from .models import HelloWorld
from .serializers import HelloWorldSerializer

class HelloWorldViewSet(viewsets.ModelViewSet):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer
