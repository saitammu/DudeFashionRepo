from django.db import models
from cloudinary.models import CloudinaryField

BADGE_CHOICES = [('HOT','HOT'),('NEW','NEW'),('SALE','SALE')]
CATEGORY_CHOICES = [
    ('Shirts','Shirts'),
    ('T-Shirts','T-Shirts'),
    ('Jeans & Pants','Jeans & Pants'),
    ('Shorts & Inners','Shorts & Inners'),
    ('Hoodies & Jackets','Hoodies & Jackets'),
]

class Product(models.Model):
    name     = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    sub      = models.CharField(max_length=100, verbose_name='Sub-category')
    price    = models.PositiveIntegerField(help_text='Selling price in ₹')
    orig     = models.PositiveIntegerField(help_text='Original/MRP price in ₹')
    badge    = models.CharField(max_length=10, choices=BADGE_CHOICES, default='NEW')
    image    = CloudinaryField('image', folder='products', blank=True, null=True)
    image_url= models.URLField(blank=True, help_text='Use URL if no file uploaded')
    active   = models.BooleanField(default=True)
    order    = models.PositiveIntegerField(default=0, help_text='Display order (lower = first)')
    created  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} ({self.category})"

    @property
    def img_src(self):
        try:
            if self.image:
                return self.image.url
        except Exception as e:
            # Handle cases where Cloudinary is not properly configured
            pass
        if self.image_url:
            return self.image_url
        return 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=600&q=80'

    @property
    def off(self):
        if self.orig > 0:
            return round((1 - self.price / self.orig) * 100)
        return 0

    @property
    def badge_class(self):
        return {'HOT':'bh','NEW':'bn','SALE':'bs'}.get(self.badge,'bn')


class Offer(models.Model):
    title      = models.CharField(max_length=200)
    subtitle   = models.CharField(max_length=300, blank=True)
    code       = models.CharField(max_length=30, blank=True, help_text='Coupon/promo code')
    discount   = models.CharField(max_length=20, help_text='e.g. 20% or ₹200 OFF')
    active     = models.BooleanField(default=True)
    created    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Offer / Promotion'
        verbose_name_plural = 'Offers & Promotions'

    def __str__(self):
        return f"{self.title} — {self.discount}"
