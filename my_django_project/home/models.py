from django.db import models

class Contact(models.Model):
    Serial_no=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Phone_no=models.CharField(max_length=13)
    Email=models.CharField(max_length=100)
    Content=models.TextField()
    Time=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return 'Querry from ' + self.Name + ' - ' + self.Email