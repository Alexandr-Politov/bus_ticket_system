from django.template.context_processors import request
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from station.models import Bus, Facility, Order, Ticket, Trip
from station.serializers import BusSerializer, TripSerializer, TripListSerializer, BusListSerializer, \
    FacilitySerializer, BusRetrieveSerializer, TripRetrieveSerializer, OrderSerializer


class BusViewSet(viewsets.ModelViewSet):
     # viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
     # mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    @staticmethod
    def _param_to_ints(query_string):
        """Converts a string of format '1,2,3' to a list of integers [1, 2, 3]"""
        return [int(str_id) for str_id in query_string.split(",")]

    def get_serializer_class(self):
        if self.action == "list":
            return BusListSerializer
        elif self.action == "retrieve":
            return BusRetrieveSerializer
        return BusSerializer

    def get_queryset(self):
        queryset = self.queryset
        facilities = self.request.query_params.get("facilities")
        if facilities:
            facilities = self._param_to_ints(facilities)
            queryset = queryset.filter(facilities__id__in=facilities)

        if self.action in ["list", "retrieve"]:
            queryset = queryset.prefetch_related("facilities")
        return queryset.distinct()


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all().select_related()

    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer
        elif self.action == "retrieve":
            return TripRetrieveSerializer
        return TripSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related("bus")
        return queryset


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
