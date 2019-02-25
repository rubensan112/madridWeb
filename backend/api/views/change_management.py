from rest_framework import viewsets, permissions
from backend.change_management.models import ChangeRequestORM, RemedyStateORM, EmailORM, AffectedEntityORM
from backend.api.serializers.ChangeRequest import ChangeRequestSerializer
from backend.api.serializers.Email import EmailSerializer
from backend.api.serializers.RemedyState import RemedyStateSerializer
from backend.api.serializers.AffectedEntity import AffectedEntitySerializer



class ChangeRequestViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ChangeRequestORM.objects.all()
    serializer_class = ChangeRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AffectedEntityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = AffectedEntityORM.objects.all()
    serializer_class = AffectedEntitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EmailViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = EmailORM.objects.all()
    serializer_class = EmailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RemedyStateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = RemedyStateORM.objects.all()
    serializer_class = RemedyStateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)