from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from .models import Product, Offer
from .custom_admin import admin_site

class ProductAdmin(ModelAdmin):
    list_display  = ('thumb','name','category','sub','price','orig','price_tag','orig_tag','off_pct','badge','active','order')
    list_editable = ('price','orig','badge','active','order')
    list_filter   = ('category','badge','active')
    search_fields = ('name','sub')
    ordering      = ('order','-created')
    save_on_top   = True
    fieldsets = (
        ('📦 Product Details', {
            'fields': ('name','category','sub','badge','active','order')
        }),
        ('💰 Pricing', {
            'fields': ('price','orig'),
            'description': 'Set the selling price and original MRP.'
        }),
        ('🖼️ Product Image', {
            'fields': ('image','image_url'),
            'description': '📤 Upload a photo from your device, OR paste an image URL below. Uploaded photo takes priority over URL.'
        }),
    )

    def thumb(self, obj):
        src = obj.img_src
        return format_html(
            '<img src="{}" style="width:52px;height:62px;object-fit:cover;border-radius:8px;border:1.5px solid #eee"/>',
            src
        )
    thumb.short_description = '📷'

    def price_tag(self, obj):
        return format_html('<strong>₹{}</strong>', obj.price)
    price_tag.short_description = 'Price'
    price_tag.admin_order_field = 'price'

    def orig_tag(self, obj):
        return format_html('<span style="color:#aaa;text-decoration:line-through">₹{}</span>', obj.orig)
    orig_tag.short_description = 'MRP'

    def off_pct(self, obj):
        pct = obj.off
        color = '#27ae60' if pct >= 20 else '#e67e22'
        return format_html('<span style="color:{};font-weight:700">{:.0f}% off</span>', color, pct)
    off_pct.short_description = 'Discount'


class OfferAdmin(ModelAdmin):
    list_display  = ('title','discount','code_badge','active','created')
    list_editable = ('active',)
    list_filter   = ('active',)
    search_fields = ('title','code')
    save_on_top   = True
    fieldsets = (
        ('🎁 Offer Details', {
            'fields': ('title','subtitle','discount','code','active'),
            'description': 'This offer banner appears on the homepage. Only one active offer is shown at a time.'
        }),
    )

    def code_badge(self, obj):
        if obj.code:
            return format_html(
                '<span style="background:#E8C547;color:#111;padding:.2rem .6rem;border-radius:50px;font-size:.75rem;font-weight:700">{}</span>',
                obj.code
            )
        return '—'
    code_badge.short_description = 'Promo Code'


admin_site.register(Product, ProductAdmin)
admin_site.register(Offer, OfferAdmin)
