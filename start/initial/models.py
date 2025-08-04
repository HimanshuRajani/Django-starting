from django.db import models as md
from django.utils import timezone
# Create your models here.
class some(md.Model):
    name = md.CharField(max_length=50)
    email = md.EmailField(null=False)
    feedback = md.TextField()
    image = md.ImageField(upload_to = 'img/')
    date = md.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.email