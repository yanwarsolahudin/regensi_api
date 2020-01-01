from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    authentication_classes = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'supplier_code'

    search_fields = [
        'name',
        'address',
        'phone',
        'pic',
    ]
    filterset_fields = ['supplier_code',]