from django.urls import path, include
from rest_framework import routers

from station.views import BusViewSet, TripViewSet, FacilityViewSet, OrderViewSet

app_name = "station"

router = routers.DefaultRouter()
router.register("buses", BusViewSet)
router.register("trips", TripViewSet)
router.register("facilities", FacilityViewSet)
router.register("orders", OrderViewSet)


# bus_list = BusViewSet.as_view(actions={"get": "list", "post": "create"})
# bus_detail = BusViewSet.as_view(actions={"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})

urlpatterns = [
    path("", include(router.urls)),
    # path("buses/", router, name="bus-list"),
    # path("buses/<int:pk>", router, name="bus-detail"),
]
