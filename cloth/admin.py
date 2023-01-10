from django.contrib.admin import site
from . import models

site.register(models.Cloth)
site.register(models.Tag)
site.register(models.Customer)
site.register(models.Order)
