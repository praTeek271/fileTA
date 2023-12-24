# fileshare/models.py
from django.db import models
from django.contrib.auth.models import User
from random import randint

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

        # Save the special URL to the download_link field
        self.download_link = special_url
        self.save()

        return special_url
