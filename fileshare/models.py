# fileshare/models.py
from django.db import models
from django.contrib.auth.models import User as DjangoUser
from random import randint

class File(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    download_link = models.CharField(max_length=255, blank=True)

    def generate_special_url(self):
        # You can customize the logic for creating a special URL here
        username = self.user.username
        filename = self.file.name
        numerals = str(randint(100000, 999999))
        # numerals = "123456789"  # Add more if needed

        # Combine username, filename, and numerals to create a special URL
        special_url = f"{username}_{numerals}_{filename}"
        print("generating url........")
        # Save the special URL to the download_link field
        self.download_link = special_url
        self.save()

        return special_url
    

    def __str__(self):
        return self.file.name



class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_field = models.FileField(upload_to='uploads/')
    desc = models.TextField()

    def __str__(self):
        return f'{self.user}=> {self.title}'