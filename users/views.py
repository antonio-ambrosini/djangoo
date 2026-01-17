from django.contrib.auth.models         import User, Group
from rest_framework                     import permissions, viewsets


from .                                  import serializers as serializers_lib


class UserViewSet(viewsets.ModelViewSet):

    queryset           = User.objects.all().order_by('-date_joined')
    serializer_class   = serializers_lib.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset           = Group.objects.all().order_by('name')
    serializer_class   = serializers_lib.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
