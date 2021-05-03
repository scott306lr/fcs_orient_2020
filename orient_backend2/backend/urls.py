# backend/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'hints', views.HintsViewSet)
router.register(r'hint', views.HintViewSet)
router.register(r'groups', views.GroupsViewSet)
router.register(r'groupsinfo', views.GroupsinfoViewSet)
router.register(r'others', views.OthersViewSet)
router.register(r'logging', views.LoggingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
            path('', include(router.urls)),
            path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
