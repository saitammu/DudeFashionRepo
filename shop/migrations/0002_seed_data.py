from django.db import migrations
from django.contrib.auth.hashers import make_password

STATIC = '/static/shop/img/'
UNS = 'https://images.unsplash.com/photo-'

def seed(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Offer   = apps.get_model('shop', 'Offer')
    User    = apps.get_model('auth', 'User')

    # ── Create superuser with fixed password dude143 ──────────
    # Allow any username — but always password = dude143
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create(
            username='admin',
            password=make_password('dude143'),
            is_superuser=True,
            is_staff=True,
            is_active=True,
            email='',
            first_name='Dude',
            last_name='Fashion',
        )

    # ── Seed products ─────────────────────────────────────────
    rows = [
        ('White Solid Casual Shirt','Shirts','Casual Shirts',999,1599,'NEW',STATIC+'download.jpeg',0),
        ('Flannel Check Shirt','Shirts','Casual Shirts',899,1399,'HOT',STATIC+'download__1_.jpeg',1),
        ('Black Printed Party Shirt','Shirts','Party Shirts',1299,1999,'HOT',STATIC+'download__2_.jpeg',2),
        ('Brown Knit Camp Shirt','Shirts','Party Shirts',1099,1699,'NEW',STATIC+'download__3_.jpeg',3),
        ('Slim Fit Grey Shirt','Shirts','Formal Shirts',849,1299,'SALE',STATIC+'download__4_.jpeg',4),
        ('Sage Green Linen Shirt','Shirts','Casual Shirts',799,1299,'NEW',STATIC+'download__5_.jpeg',5),
        ('Varsity Polo Tee','T-Shirts','Polo T-Shirts',649,999,'HOT',STATIC+'images__5_.jpeg',6),
        ('Purple Graphic Tee','T-Shirts','Printed Tees',549,849,'NEW',STATIC+'download__15_.jpeg',7),
        ('Tie-Dye Oversized Tee','T-Shirts','Oversized Tees',699,1099,'HOT',STATIC+'download__14_.jpeg',8),
        ('Fearless Graphic Tee','T-Shirts','Printed Tees',599,899,'SALE',STATIC+'download__13_.jpeg',9),
        ('Metamorphosis Back Print Tee','T-Shirts','Oversized Tees',749,1199,'NEW',STATIC+'download__12_.jpeg',10),
        ('Dreams Of Veins Tee','T-Shirts','Plain T-Shirts',499,799,'HOT',STATIC+'images__13_.jpeg',11),
        ('Ripped Straight Jeans','Jeans & Pants','Jeans',1299,1999,'HOT',STATIC+'download__6_.jpeg',12),
        ('Cargo Jogger Jeans','Jeans & Pants','Joggers',1199,1799,'NEW',STATIC+'download__7_.jpeg',13),
        ('Baggy Distressed Jeans','Jeans & Pants','Jeans',1399,2099,'NEW',STATIC+'download__8_.jpeg',14),
        ('Slim Fit Blue Jeans','Jeans & Pants','Jeans',999,1499,'SALE',STATIC+'download__9_.jpeg',15),
        ('Classic Dark Wash Jeans','Jeans & Pants','Jeans',1199,1799,'HOT',STATIC+'download__10_.jpeg',16),
        ('Tapered Light Wash Jeans','Jeans & Pants','Jeans',999,1499,'NEW',STATIC+'download__11_.jpeg',17),
        ('Wide Leg Baggy Jeans','Jeans & Pants','Jeans',1299,1999,'HOT',STATIC+'images__6_.jpeg',18),
        ('Straight Fit Faded Jeans','Jeans & Pants','Jeans',1099,1699,'SALE',STATIC+'images__7_.jpeg',19),
        ('Relaxed Straight Jeans','Jeans & Pants','Jeans',1199,1799,'NEW',STATIC+'images__8_.jpeg',20),
        ('Comfort Fit Light Jeans','Jeans & Pants','Jeans',999,1499,'HOT',STATIC+'images__9_.jpeg',21),
        ('Powder Blue Chinos','Jeans & Pants','Chinos',899,1399,'NEW',STATIC+'images__10_.jpeg',22),
        ('Heavy Ripped Jeans','Jeans & Pants','Jeans',1399,2199,'HOT',STATIC+'images__11_.jpeg',23),
        ('Loose Fit Regular Jeans','Jeans & Pants','Jeans',1099,1699,'SALE',STATIC+'images__12_.jpeg',24),
        ('Sage Green Cargo Pants','Jeans & Pants','Joggers',1099,1699,'NEW',UNS+'1552902865-b72c031ac5ea?auto=format&fit=crop&w=600&q=80',25),
        ('Cargo Shorts','Shorts & Inners','Shorts',699,1099,'HOT',UNS+'1598033129183-c4f50c736f10?auto=format&fit=crop&w=600&q=80',26),
        ('Cotton Boxer Briefs (Pack 3)','Shorts & Inners','Inners',499,799,'NEW',UNS+'1616087949951-c7e4bf2b8cba?auto=format&fit=crop&w=600&q=80',27),
        ('Athletic Shorts','Shorts & Inners','Shorts',599,899,'SALE',UNS+'1546961342-ea5f62d5a27b?auto=format&fit=crop&w=600&q=80',28),
        ('Oversized Hoodie','Hoodies & Jackets','Hoodies',1399,1999,'NEW',UNS+'1556821840-3a63f15732ce?auto=format&fit=crop&w=600&q=80',29),
        ('Denim Jacket','Hoodies & Jackets','Jackets',1899,2799,'HOT',UNS+'1601333144130-8cbb312386b6?auto=format&fit=crop&w=600&q=80',30),
        ('Slim Fit Blazer','Hoodies & Jackets','Blazers',2499,3999,'SALE',UNS+'1594938298603-c8148c4b36b7?auto=format&fit=crop&w=600&q=80',31),
    ]
    for name,cat,sub,price,orig,badge,img_url,order in rows:
        Product.objects.get_or_create(
            name=name,
            defaults=dict(category=cat,sub=sub,price=price,orig=orig,
                          badge=badge,image_url=img_url,order=order,active=True)
        )

    # ── Seed default offer ────────────────────────────────────
    Offer.objects.get_or_create(
        title='Grand Opening Offer',
        defaults=dict(
            subtitle='Use code at checkout — limited time deal!',
            code='DUDE20',
            discount='20% OFF',
            active=True,
        )
    )

def unseed(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [('shop', '0001_initial'), ('auth', '0001_initial')]
    operations = [migrations.RunPython(seed, unseed)]
