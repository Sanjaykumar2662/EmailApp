from django.db import models

class Uploaded_File(models.Model):
    file_name = models.CharField(max_length=255)
    file_content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
