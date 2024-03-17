from django.db import models

class StudentModel(models.Model):
    roll_no = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=20)
    marks = models.IntegerField()
    Department_Name  = models.CharField(max_length=30 , default = None)
    email = models.EmailField()
    upload_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name
