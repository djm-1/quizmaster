from django.db import models

# Create your models here.
class quiz(models.Model):
    id=models.AutoField
    question=models.TextField(default="")
    option_1=models.CharField(max_length=300,default="")
    option_2=models.CharField(max_length=300,default="")
    option_3=models.CharField(max_length=300,default="")
    option_4=models.CharField(max_length=300,default="")
    answer=models.CharField(max_length=300,default="")
    

    def __str__(self):
        return self.question