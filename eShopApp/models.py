from django.db import models
from django.contrib.auth.models import User

class ProductType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot turi'
        verbose_name_plural = 'Mahsulot turlari'

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    price = models.PositiveBigIntegerField()
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

class MoreImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Ko'proq rasm"
        verbose_name_plural = "Ko'proq rasmlar"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    is_shipped = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    def __str__(self):
        return f"{str(self.product)} / {self.quantity}ta / {self.user}"

class Shipping(models.Model):

    class StatusChoice(models.TextChoices):
        Pending = "P", "Yig'ilayabdi"
        Ready = "R", "Yo'lda"
        Delivered = "D", "Yetkazildi"

    order = models.ManyToManyField(Order, related_name='shipping_order', blank=True)
    time = models.DateTimeField(auto_now_add=True)
    adress = models.TextField(max_length=1000)
    contact_for = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=StatusChoice.choices, default=StatusChoice.Pending)
    total_price = models.PositiveBigIntegerField()
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Yetkazib berish"
        verbose_name_plural = "Yetkazib berish"