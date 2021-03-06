from django.db import models
from django.conf import settings
# Create your models here.
CATEGORY_CHOICES = (
    ('S', 'SHIRT'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),

)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')

)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    catogory = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    itmes = models. ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    odered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
