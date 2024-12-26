from django.core.files import File
from django.db import models
from io import BytesIO
from PIL import Image
import uuid, base64

# Create your models here.
# category models
class Category(models.Model):
    name = models.CharField (max_length = 255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories '

    def __str__(self) -> str:
        return self.name
    # function to return the slug of a category (url)
    def get_absolute_url(self):
        return f'/{self.slug}/'


# key feature model for creating key features
class KeyFeature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=12, editable=False, unique=True)
    category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    key_features = models.ManyToManyField(KeyFeature, related_name='products')
    # passing an attribute called key_features into the 
    


    class Meta:
        ordering = ('-date_added',)

    def __str__(self) -> str:
        return self.name
     
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def save(self, *args, **kwargs):
        if not self.id:
            
            hex_string = uuid.uuid4().hex
            bytes_data = bytes.fromhex(hex_string)
            data = base64.urlsafe_b64encode(bytes_data).decode('ascii')[:12]
            self.id = data.replace("-", "")
        return super().save(*args, **kwargs)
    


