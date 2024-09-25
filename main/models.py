from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
