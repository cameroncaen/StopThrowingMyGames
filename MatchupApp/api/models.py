from django.db import models
import string, random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Match.objects.filter(code=code).count() == 0:
            break

    return code
# Create your models here.
class Match(models.Model):
    host = models.CharField(max_length=16, default="", unique=True)
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)

    username = models.CharField(max_length=16, default="")
    tag = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)