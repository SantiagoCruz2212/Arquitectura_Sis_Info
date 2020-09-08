from django.http import HttpResponse

#API Rest imports
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from betterchoise.serializers import UserSerializer, GroupSerializer

#API Rest
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#paginitas personales

def index(request):
    return HttpResponse("hola mundo :)")

def papaperuana(request):
    return HttpResponse("hola mundo peruano :)")
