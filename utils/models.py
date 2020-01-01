import datetime

from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def generate_string_code(model):
    count = model.objects.all().count() + 1

    date_now = datetime.datetime.now().strftime('%d-%m-%Y')
    len_count = len(str(count))

    if len_count == 1:
        result = f'{model.PREFIX}-{date_now}-0000{count}'
    elif len_count == 2:
        result = f'{model.PREFIX}-{date_now}-000{count}'
    elif len_count == 3:
        result = f'{model.PREFIX}-{date_now}-00{count}'
    elif len_count == 4:
        result = f'{model.PREFIX}-{date_now}-0{count}'
    elif len_count == 5:
        result = f'{model.PREFIX}-{date_now}-{count}'
    else:
        result = None

    return result