from rest_framework import viewsets, permissions
from backend.work_management.models import WorkProgrammedORM
from backend.api.serializers.WorkProgrammed import WorkProgrammedSerializer



class WorkProgrammedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = WorkProgrammedORM.objects.all()
    serializer_class = WorkProgrammedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)