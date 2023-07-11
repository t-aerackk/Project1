from django.db import models

class EmployeeInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Phone=models.BigIntegerField()

    def __str__(self):
        names = sorted([self.first_name, self.last_name])
        return f"{names[0]} {names[1]}"

# class EmployeeInfo(models.Model):
#     last_name = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=200)

#     def __str__(self):
#         return f"{self.last_name}, {self.first_name}"
class ImageHandler(models.Model):
    image=models.ImageField(upload_to='images/')
