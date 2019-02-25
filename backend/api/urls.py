"""
Routes and urls for application api.

Should contain an attribute called urlpatterns,
and should be an iterable (preferably a list).
"""
from django.conf.urls import url, include
from rest_framework import routers

from backend.api.views import change_management, work_management

'''
Actions are only bound to methods at the point of instantiating the views.

    user_list = UserViewSet.as_view({'get': 'list'})
    user_detail = UserViewSet.as_view({'get': 'retrieve'})

Typically, rather than instantiate views from viewsets directly, you'll
register the viewset with a router and let the URL conf be determined
automatically.

    router = DefaultRouter()
    router.register(r'users', UserViewSet, 'user')
    urlpatterns = router.urls
"""

'''



change_management_router = routers.DefaultRouter()
change_management_router.register(r'ChangeRequest', change_management.ChangeRequestViewSet)
change_management_router.register(r'Email', change_management.EmailViewSet)
change_management_router.register(r'RemedyState', change_management.RemedyStateViewSet)
change_management_router.register(r'AffectedEntity', change_management.AffectedEntityViewSet)

work_management_router = routers.DefaultRouter()
work_management_router.register(r'WorkProgrammed', work_management.WorkProgrammedViewSet)

urlpatterns = [
    url(r'^WorkManagement/', include(work_management_router.urls)),
    url(r'^ChangeManagement/', include(change_management_router.urls)),
]