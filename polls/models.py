from django.db import models

# Create your models here.
class KundalikModel(models.Model):
    name = models.CharField(max_length=120,default=' ')
    desc = models.TextField()
    status = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name
    
