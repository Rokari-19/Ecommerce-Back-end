from django.db import models
from django.contrib.auth import get_user_model
import uuid, base64
# Create your models here.
User = get_user_model()

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    id = models.CharField(max_length=12, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            
            hex_string = uuid.uuid4().hex
            bytes_data = bytes.fromhex(hex_string)
            data = base64.urlsafe_b64encode(bytes_data).decode('ascii')[:12]
            self.id = data.replace("-", "")
        return super().save(*args, **kwargs)