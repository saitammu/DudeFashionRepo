from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Shirts','Shirts'),('T-Shirts','T-Shirts'),('Jeans & Pants','Jeans & Pants'),('Shorts & Inners','Shorts & Inners'),('Hoodies & Jackets','Hoodies & Jackets')], max_length=50)),
                ('sub', models.CharField(max_length=100, verbose_name='Sub-category')),
                ('price', models.PositiveIntegerField(help_text='Selling price in ₹')),
                ('orig', models.PositiveIntegerField(help_text='Original/MRP price in ₹')),
                ('badge', models.CharField(choices=[('HOT','HOT'),('NEW','NEW'),('SALE','SALE')], default='NEW', max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image_url', models.URLField(blank=True, help_text='Use URL if no file uploaded')),
                ('active', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(default=0, help_text='Display order (lower = first)')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['order', '-created'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, max_length=300)),
                ('code', models.CharField(blank=True, help_text='Coupon/promo code', max_length=30)),
                ('discount', models.CharField(help_text='e.g. 20% or ₹200 OFF', max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created'], 'verbose_name': 'Offer / Promotion', 'verbose_name_plural': 'Offers & Promotions'},
        ),
    ]
