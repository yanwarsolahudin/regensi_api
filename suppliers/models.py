from django.db import models

from utils.models import Timestamp, generate_string_code


class Supplier(Timestamp):
    PREFIX = 'SPR'

    supplier_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default='Ex: Firda Firdaus')
    address = models.TextField()
    phone = models.CharField(max_length=20, default='Ex: +6299999999')
    pic = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.supplier_code:
            # Newly created object, so set slug
            self.supplier_code = generate_string_code(Supplier)

        super(Supplier, self).save(*args, **kwargs)

    def __str__(self):
        return self.supplier_code
