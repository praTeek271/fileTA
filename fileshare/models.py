# models.py
from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=10)  # To store file type (pptx, docx, xlsx)
    is_encrypted = models.BooleanField(default=False)
    download_link = models.CharField(max_length=100, blank=True)
