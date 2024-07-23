from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Arranging in descending order
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    # related_name='items': This creates a reverse relation. It allows you to do things like user.items.all() to get all items created by a specific user.
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    # CASCADE means that if a User is deleted, all items created by that user will also be deleted.
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name