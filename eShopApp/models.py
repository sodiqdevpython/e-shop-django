from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tel_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profillar'

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

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_product')
    body = models.TextField(max_length=130)
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Koment'
        verbose_name_plural = 'Komentlar'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    def __str__(self):
        return str(self.user)

class Shipping(models.Model):

    class StatusChoice(models.TextChoices):
        Pending = "P", "Yig'ilayabdi"
        Ready = "R", "Yo'lda"
        Delivered = "D", "Yetkazildi"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipping_order')
    time = models.DateTimeField(auto_now_add=True)
    adress = models.TextField(max_length=1000)
    contact_for = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=StatusChoice.choices, default=StatusChoice.Pending)

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = "Yetkazib berish"
        verbose_name_plural = "Yetkazib berish"