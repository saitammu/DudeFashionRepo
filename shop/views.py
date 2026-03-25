from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, Offer

WA_NUMBER = '919381473698'
SHOP_INFO = {
    'name': 'DUDE FASHION',
    'address': 'Sivaraopeta, Tammi Raju Nagar, Bhimavaram, Andhra Pradesh 534202',
    'phone': '+91 93814 73698',
    'hours': '10:00 AM – 10:00 PM, Every Day',
    'rating': '5.0',
    'maps_url': 'https://maps.app.goo.gl/nfqh38q2bpHZrp9G7',
    'wa_number': WA_NUMBER,
}

STATIC_IMG = '/static/shop/img/'

# ── Fallback products (used only when DB is empty) ────────────
FALLBACK_PRODUCTS = [
    # ── Shirts ──────────────────────────────────────────────────
    {'id':1, 'name':'White Solid Casual Shirt',      'cat':'Shirts', 'sub':'Casual Shirts',  'price':999,  'orig':1599, 'badge':'NEW', 'img':STATIC_IMG+'download.jpeg'},
    {'id':2, 'name':'Flannel Check Shirt',            'cat':'Shirts', 'sub':'Casual Shirts',  'price':899,  'orig':1399, 'badge':'HOT', 'img':STATIC_IMG+'download__1_.jpeg'},
    {'id':3, 'name':'Black Printed Party Shirt',      'cat':'Shirts', 'sub':'Party Shirts',   'price':1299, 'orig':1999, 'badge':'HOT', 'img':STATIC_IMG+'download__2_.jpeg'},
    {'id':4, 'name':'Brown Knit Camp Shirt',          'cat':'Shirts', 'sub':'Party Shirts',   'price':1099, 'orig':1699, 'badge':'NEW', 'img':STATIC_IMG+'download__3_.jpeg'},
    {'id':5, 'name':'Slim Fit Grey Shirt',            'cat':'Shirts', 'sub':'Formal Shirts',  'price':849,  'orig':1299, 'badge':'SALE','img':STATIC_IMG+'download__4_.jpeg'},
    {'id':6, 'name':'Sage Green Linen Shirt',         'cat':'Shirts', 'sub':'Casual Shirts',  'price':799,  'orig':1299, 'badge':'NEW', 'img':STATIC_IMG+'download__5_.jpeg'},

    # ── More Shirts ──────────────────────────────────────────────────
    {'id':51, 'name':'Green Madras Check Shirt',       'cat':'Shirts','sub':'Casual Shirts',  'price':999, 'orig':1599,'badge':'NEW', 'img':STATIC_IMG+'images__17_.jpeg'},
    {'id':52, 'name':'Brown Sheer Casual Shirt',       'cat':'Shirts','sub':'Casual Shirts',  'price':849, 'orig':1299,'badge':'HOT', 'img':STATIC_IMG+'images__18_.jpeg'},
    {'id':53, 'name':'Sage Green Solid Shirt',         'cat':'Shirts','sub':'Formal Shirts',  'price':899, 'orig':1399,'badge':'NEW', 'img':STATIC_IMG+'download__24_.jpeg'},
    {'id':54, 'name':'Dark Green Cuban Shirt',         'cat':'Shirts','sub':'Party Shirts',   'price':1199,'orig':1799,'badge':'HOT', 'img':STATIC_IMG+'download__25_.jpeg'},
    {'id':55, 'name':'Grey Slim Formal Shirt',         'cat':'Shirts','sub':'Formal Shirts',  'price':849, 'orig':1299,'badge':'NEW', 'img':STATIC_IMG+'download__26_.jpeg'},
    {'id':56, 'name':'White Linen Casual Shirt',       'cat':'Shirts','sub':'Casual Shirts',  'price':999, 'orig':1499,'badge':'HOT', 'img':STATIC_IMG+'download__27_.jpeg'},
    {'id':57, 'name':'Green Ombre Check Shirt',        'cat':'Shirts','sub':'Casual Shirts',  'price':1099,'orig':1599,'badge':'NEW', 'img':STATIC_IMG+'download__28_.jpeg'},
    {'id':58, 'name':'Navy Blue Ikat Print Shirt',     'cat':'Shirts','sub':'Party Shirts',   'price':1299,'orig':1999,'badge':'HOT', 'img':STATIC_IMG+'download__29_.jpeg'},
    {'id':59, 'name':'Mauve Ribbed Casual Shirt',      'cat':'Shirts','sub':'Casual Shirts',  'price':949, 'orig':1449,'badge':'NEW', 'img':STATIC_IMG+'download__30_.jpeg'},
    {'id':60, 'name':'Blue Ombre Check Shirt',         'cat':'Shirts','sub':'Casual Shirts',  'price':999, 'orig':1499,'badge':'SALE','img':STATIC_IMG+'download__31_.jpeg'},

    # ── T-Shirts ─────────────────────────────────────────────────
    {'id':7,  'name':'Varsity Polo Tee',              'cat':'T-Shirts','sub':'Polo T-Shirts', 'price':649, 'orig':999,  'badge':'HOT', 'img':STATIC_IMG+'images__5_.jpeg'},
    {'id':8,  'name':'Purple Graphic Tee',            'cat':'T-Shirts','sub':'Printed Tees',  'price':549, 'orig':849,  'badge':'NEW', 'img':STATIC_IMG+'download__15_.jpeg'},
    {'id':9,  'name':'Tie-Dye Oversized Tee',         'cat':'T-Shirts','sub':'Oversized Tees','price':699, 'orig':1099, 'badge':'HOT', 'img':STATIC_IMG+'download__14_.jpeg'},
    {'id':10, 'name':'Fearless Graphic Tee',          'cat':'T-Shirts','sub':'Printed Tees',  'price':599, 'orig':899,  'badge':'SALE','img':STATIC_IMG+'download__13_.jpeg'},
    {'id':11, 'name':'Metamorphosis Back Print Tee',  'cat':'T-Shirts','sub':'Oversized Tees','price':749, 'orig':1199, 'badge':'NEW', 'img':STATIC_IMG+'download__12_.jpeg'},
    {'id':12, 'name':'Dreams Of Veins Tee',           'cat':'T-Shirts','sub':'Plain T-Shirts','price':499, 'orig':799,  'badge':'HOT', 'img':STATIC_IMG+'images__13_.jpeg'},

    # ── More T-Shirts ────────────────────────────────────────────────
    {'id':61, 'name':'Black Stripe Crew Tee',          'cat':'T-Shirts','sub':'Plain T-Shirts','price':549,'orig':849, 'badge':'NEW', 'img':STATIC_IMG+'download__32_.jpeg'},
    {'id':62, 'name':'Olive Pocket Crew Tee',          'cat':'T-Shirts','sub':'Plain T-Shirts','price':499,'orig':799, 'badge':'HOT', 'img':STATIC_IMG+'download__33_.jpeg'},
    {'id':63, 'name':'Navy Brown Colourblock Polo',    'cat':'T-Shirts','sub':'Polo T-Shirts', 'price':699,'orig':1099,'badge':'NEW', 'img':STATIC_IMG+'download__34_.jpeg'},
    {'id':64, 'name':'Grey Stripe Graphic Tee',        'cat':'T-Shirts','sub':'Printed Tees',  'price':599,'orig':899, 'badge':'HOT', 'img':STATIC_IMG+'images__19_.jpeg'},
    {'id':65, 'name':'Classic White Crew Tee 3-Pack',  'cat':'T-Shirts','sub':'Plain T-Shirts','price':899,'orig':1399,'badge':'SALE','img':STATIC_IMG+'images__20_.jpeg'},
    {'id':66, 'name':'Beige Long Sleeve Tee',          'cat':'T-Shirts','sub':'Plain T-Shirts','price':649,'orig':999, 'badge':'NEW', 'img':STATIC_IMG+'images__21_.jpeg'},
    {'id':67, 'name':'Navy Gradient Stripe Polo',      'cat':'T-Shirts','sub':'Polo T-Shirts', 'price':749,'orig':1149,'badge':'HOT', 'img':STATIC_IMG+'images__22_.jpeg'},

    # ── Jeans & Pants ─────────────────────────────────────────────
    {'id':13, 'name':'Ripped Straight Jeans',         'cat':'Jeans & Pants','sub':'Jeans',   'price':1299,'orig':1999, 'badge':'HOT', 'img':STATIC_IMG+'download__6_.jpeg'},
    {'id':14, 'name':'Cargo Jogger Jeans',            'cat':'Jeans & Pants','sub':'Joggers',  'price':1199,'orig':1799, 'badge':'NEW', 'img':STATIC_IMG+'download__7_.jpeg'},
    {'id':15, 'name':'Baggy Distressed Jeans',        'cat':'Jeans & Pants','sub':'Jeans',   'price':1399,'orig':2099, 'badge':'NEW', 'img':STATIC_IMG+'download__8_.jpeg'},
    {'id':16, 'name':'Slim Fit Blue Jeans',           'cat':'Jeans & Pants','sub':'Jeans',   'price':999, 'orig':1499, 'badge':'SALE','img':STATIC_IMG+'download__9_.jpeg'},
    {'id':17, 'name':'Classic Dark Wash Jeans',       'cat':'Jeans & Pants','sub':'Jeans',   'price':1199,'orig':1799, 'badge':'HOT', 'img':STATIC_IMG+'download__10_.jpeg'},
    {'id':18, 'name':'Tapered Light Wash Jeans',      'cat':'Jeans & Pants','sub':'Jeans',   'price':999, 'orig':1499, 'badge':'NEW', 'img':STATIC_IMG+'download__11_.jpeg'},
    {'id':19, 'name':'Wide Leg Baggy Jeans',          'cat':'Jeans & Pants','sub':'Jeans',   'price':1299,'orig':1999, 'badge':'HOT', 'img':STATIC_IMG+'images__6_.jpeg'},
    {'id':20, 'name':'Straight Fit Faded Jeans',      'cat':'Jeans & Pants','sub':'Jeans',   'price':1099,'orig':1699, 'badge':'SALE','img':STATIC_IMG+'images__7_.jpeg'},
    {'id':21, 'name':'Relaxed Straight Jeans',        'cat':'Jeans & Pants','sub':'Jeans',   'price':1199,'orig':1799, 'badge':'NEW', 'img':STATIC_IMG+'images__8_.jpeg'},
    {'id':22, 'name':'Comfort Fit Light Jeans',       'cat':'Jeans & Pants','sub':'Jeans',   'price':999, 'orig':1499, 'badge':'HOT', 'img':STATIC_IMG+'images__9_.jpeg'},
    {'id':23, 'name':'Powder Blue Chinos',            'cat':'Jeans & Pants','sub':'Chinos',  'price':899, 'orig':1399, 'badge':'NEW', 'img':STATIC_IMG+'images__10_.jpeg'},
    {'id':24, 'name':'Heavy Ripped Jeans',            'cat':'Jeans & Pants','sub':'Jeans',   'price':1399,'orig':2199, 'badge':'HOT', 'img':STATIC_IMG+'images__11_.jpeg'},
    {'id':25, 'name':'Loose Fit Regular Jeans',       'cat':'Jeans & Pants','sub':'Jeans',   'price':1099,'orig':1699, 'badge':'SALE','img':STATIC_IMG+'images__12_.jpeg'},

    # ── Shorts & Inners ───────────────────────────────────────────
    {'id':27, 'name':'Khaki Drawstring Shorts',       'cat':'Shorts & Inners','sub':'Shorts', 'price':699, 'orig':1099,'badge':'HOT', 'img':STATIC_IMG+'s0.jpeg'},
    {'id':28, 'name':'Grey Casual Shorts',            'cat':'Shorts & Inners','sub':'Shorts', 'price':599, 'orig':899, 'badge':'NEW', 'img':STATIC_IMG+'s1.jpeg'},
    {'id':29, 'name':'Beige Cargo Shorts',            'cat':'Shorts & Inners','sub':'Cargo Shorts','price':799,'orig':1199,'badge':'HOT','img':STATIC_IMG+'s2.jpeg'},
    {'id':30, 'name':'Navy Sport Shorts',             'cat':'Shorts & Inners','sub':'Shorts', 'price':549, 'orig':849, 'badge':'SALE','img':STATIC_IMG+'s3.jpeg'},
    {'id':31, 'name':'Sky Blue Terry Shorts',         'cat':'Shorts & Inners','sub':'Shorts', 'price':649, 'orig':999, 'badge':'NEW', 'img':STATIC_IMG+'s4.jpeg'},
    {'id':32, 'name':'Black Cargo Shorts',            'cat':'Shorts & Inners','sub':'Cargo Shorts','price':849,'orig':1299,'badge':'HOT','img':STATIC_IMG+'s5.jpeg'},
    {'id':33, 'name':'Khaki Slim Cargo Shorts',       'cat':'Shorts & Inners','sub':'Cargo Shorts','price':749,'orig':1149,'badge':'NEW','img':STATIC_IMG+'s6.jpeg'},
    {'id':34, 'name':'Olive Active Shorts',           'cat':'Shorts & Inners','sub':'Shorts', 'price':599, 'orig':899, 'badge':'SALE','img':STATIC_IMG+'s7.jpeg'},
    {'id':35, 'name':'Black Stripe Sport Shorts',     'cat':'Shorts & Inners','sub':'Shorts', 'price':649, 'orig':999, 'badge':'HOT', 'img':STATIC_IMG+'s8.jpeg'},
    {'id':36, 'name':'Cream Chino Shorts',            'cat':'Shorts & Inners','sub':'Shorts', 'price':699, 'orig':1099,'badge':'NEW', 'img':STATIC_IMG+'s9.jpeg'},
    {'id':37, 'name':'Navy Boxer Shorts',             'cat':'Shorts & Inners','sub':'Inners', 'price':399, 'orig':599, 'badge':'NEW', 'img':STATIC_IMG+'s11.jpeg'},

    # ── Hoodies & Jackets ─────────────────────────────────────────
    {'id':40, 'name':'Black Eternal Hoodie',          'cat':'Hoodies & Jackets','sub':'Hoodies','price':1399,'orig':1999,'badge':'HOT','img':STATIC_IMG+'download__16_.jpeg'},
    {'id':41, 'name':'Brown Essential Hoodie',        'cat':'Hoodies & Jackets','sub':'Hoodies','price':1299,'orig':1899,'badge':'NEW','img':STATIC_IMG+'download__17_.jpeg'},
    {'id':42, 'name':'Maroon Graphic Hoodie',         'cat':'Hoodies & Jackets','sub':'Hoodies','price':1499,'orig':2199,'badge':'HOT','img':STATIC_IMG+'download__18_.jpeg'},
    {'id':43, 'name':'Steel Blue Print Hoodie',       'cat':'Hoodies & Jackets','sub':'Hoodies','price':1399,'orig':1999,'badge':'NEW','img':STATIC_IMG+'download__19_.jpeg'},
    {'id':44, 'name':'Charcoal Pullover Hoodie',      'cat':'Hoodies & Jackets','sub':'Hoodies','price':1249,'orig':1799,'badge':'SALE','img':STATIC_IMG+'images__14_.jpeg'},
    {'id':45, 'name':'Navy Custom Print Hoodie',      'cat':'Hoodies & Jackets','sub':'Hoodies','price':1199,'orig':1799,'badge':'HOT', 'img':STATIC_IMG+'download__20_.jpeg'},
    {'id':46, 'name':'Black Hooded Tee',              'cat':'Hoodies & Jackets','sub':'Hoodies','price':899, 'orig':1299,'badge':'NEW', 'img':STATIC_IMG+'download__21_.jpeg'},
    {'id':47, 'name':'California Colourblock Hoodie', 'cat':'Hoodies & Jackets','sub':'Hoodies','price':1349,'orig':1999,'badge':'HOT', 'img':STATIC_IMG+'download__22_.jpeg'},
    {'id':48, 'name':'Olive Oversized Short Hoodie',  'cat':'Hoodies & Jackets','sub':'Hoodies','price':1299,'orig':1899,'badge':'NEW', 'img':STATIC_IMG+'download__23_.jpeg'},
    # ── Uploaded Media Products ─────────────────────────────────────────
    {'id':101, 'name':'New Trend Shirt',          'cat':'Shirts','sub':'Casual Shirts','price':999,'orig':1499,'badge':'NEW','img':'/media/products/images_15.jpeg'},
    {'id':102, 'name':'Cool Summer Tee',          'cat':'T-Shirts','sub':'Printed Tees','price':599,'orig':899,'badge':'HOT','img':'/media/products/images_16.jpeg'},
    {'id':103, 'name':'Denim Ripped Jeans',       'cat':'Jeans & Pants','sub':'Jeans', 'price':1299,'orig':1899,'badge':'NEW','img':'/media/products/images_21.jpeg'},
    {'id':104, 'name':'Active Sports Shorts',     'cat':'Shorts & Inners','sub':'Shorts','price':499,'orig':799,'badge':'SALE','img':'/media/products/s1.jpeg'},
    {'id':105, 'name':'Premium Winter Hoodie',    'cat':'Hoodies & Jackets','sub':'Hoodies','price':1599,'orig':2299,'badge':'HOT','img':'/media/products/download_16.jpeg'},
]

for p in FALLBACK_PRODUCTS:
    p['off']         = round((1 - p['price'] / p['orig']) * 100)
    p['badge_class'] = {'HOT': 'bh', 'NEW': 'bn', 'SALE': 'bs'}.get(p['badge'], 'bn')


def _db_products_to_dicts(qs):
    result = []
    for p in qs:
        result.append({
            'id':          p.pk,
            'name':        p.name,
            'cat':         p.category,
            'sub':         p.sub,
            'price':       p.price,
            'orig':        p.orig,
            'badge':       p.badge,
            'off':         p.off,
            'badge_class': p.badge_class,
            'img':         p.img_src,
        })
    return result


def _get_products():
    """Return products from DB if any exist, else fallback list."""
    try:
        qs = Product.objects.filter(active=True)
        if qs.exists():
            return _db_products_to_dicts(qs)
    except Exception:
        pass
    return FALLBACK_PRODUCTS


def _build_cat_subs(products):
    cat_subs = {}
    for p in products:
        cat_subs.setdefault(p['cat'], set()).add(p['sub'])
    return {k: sorted(v) for k, v in cat_subs.items()}


def index(request):
    try:
        # Pass ALL active offers, not just one
        offers = list(Offer.objects.filter(active=True))
    except Exception:
        offers = []
    return render(request, 'shop/index.html', {
        'shop':   SHOP_INFO,
        'wa':     WA_NUMBER,
        'offers': offers,
        # keep 'offer' for backward compat with any {% if offer %} checks
        'offer':  offers[0] if offers else None,
    })


def shop_view(request):
    cat_filter = request.GET.get('cat', '')
    sort_by    = request.GET.get('sort', '')
    page_num   = request.GET.get('page', 1)

    all_products = _get_products()
    products     = all_products[:]

    if cat_filter:
        products = [p for p in products if p['cat'] == cat_filter]

    if sort_by == 'low':
        products.sort(key=lambda x: x['price'])
    elif sort_by == 'high':
        products.sort(key=lambda x: x['price'], reverse=True)
    elif sort_by == 'off':
        products.sort(key=lambda x: x['off'], reverse=True)

    cat_subs = _build_cat_subs(all_products)

    paginator = Paginator(products, 12)
    page_obj  = paginator.get_page(page_num)

    return render(request, 'shop/shop.html', {
        'page_obj':     page_obj,
        'products':     list(page_obj),
        'all_products': all_products,
        'categories':   list(cat_subs.keys()),
        'cat_subs':     cat_subs,
        'shop':         SHOP_INFO,
        'wa':           WA_NUMBER,
        'cat_filter':   cat_filter,
        'sort_by':      sort_by,
        'total_count':  paginator.count,
    })


def contact_view(request):
    return render(request, 'shop/contact.html', {
        'shop': SHOP_INFO,
        'wa': WA_NUMBER,
    })

