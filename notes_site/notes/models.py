from django.db import models

# Create your models here.
class Notes(models.Model):
    note_title=models.CharField(max_length=300)
    note_content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)


