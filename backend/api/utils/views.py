from rest_framework.viewsets import ViewSet


class CustomViewSet(ViewSet):
    lookup_value_regex = '[^/]+'
