from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ("На обработке", "На обработке"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Достален"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cloth = models.ForeignKey(
        Cloth, on_delete=models.CASCADE, related_name="order_cloth"
    )
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.cloth.name
