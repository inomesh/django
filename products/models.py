from django.db import models
from django.db.models.fields import IntegerField

from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL
class Products(models.Model):
    # id = models.AutoField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)

