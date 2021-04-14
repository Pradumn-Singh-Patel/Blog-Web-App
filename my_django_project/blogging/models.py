from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    Serial_no=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=255)
    Author=models.CharField(max_length=20)
    Slug=models.CharField(max_length=150)
    Timestamp=models.DateTimeField(blank=True)
    Content=models.TextField()

    def __str__(self):
        return self.Title + ' by ' + self.Author

class blog_comment(models.Model):
    Serial_no=models.AutoField(primary_key=True)
    Comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    Parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    Time_stamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.Comment[0:13] + "..." + "by" + " " + self.user.username