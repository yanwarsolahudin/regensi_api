from rest_framework import serializers

from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'supplier_code',
            'name',
            'address',
            'phone',
            'pic',
        ]

        read_only_fields = ['supplier_code',]