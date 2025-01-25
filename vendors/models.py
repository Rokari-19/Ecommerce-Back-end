from django.db import models
from django.template.defaultfilters import slugify
import uuid, base64

# Create your models here.
from django.contrib.auth.models import User

class Vendor(models.Model):
    class Meta:
        ordering = ('store_name',)
        
    id = models.CharField(primary_key=True, max_length=12, editable=False, unique=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendors')
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=250)
    store_name = models.CharField(max_length=70, default=None)
    slug = models.SlugField(editable=False)
    
    def get_absolute_url(self):
        return f"{self.slug}"
    
    def __str__(self):
        return self.store_name
    
    def save(self, *args, **kwargs):
        if not self.id: 
            hex_string = uuid.uuid4().hex
            bytes_data = bytes.fromhex(hex_string)
            data = base64.urlsafe_b64encode(bytes_data).decode('ascii')[:12]
            self.id = data.replace("-", "")
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)