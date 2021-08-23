from django.db import models
  
# Create your models here.
  
  
class React(models.Model):
    name = models.CharField(max_length=30,blank=True, null=True)
    email =models.EmailField(max_length=30,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=30,blank=True, null=True)
    detail = models.CharField(max_length=500,blank=True, null=True)

    def __str__(self) -> str:
        return self.name


