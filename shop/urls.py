from django.urls import path
from . import views
from . import panel_views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop_view, name='shop'),
    path('contact/', views.contact_view, name='contact'),

    # ── Manager Panel ──────────────────────────────────────
    path('panel/',              panel_views.panel_login,          name='panel_login'),
    path('panel/logout/',       panel_views.panel_logout,         name='panel_logout'),
    path('panel/dashboard/',    panel_views.panel_dashboard,      name='panel_dashboard'),

    # Products
    path('panel/products/',          panel_views.panel_products,       name='panel_products'),
    path('panel/products/add/',      panel_views.panel_add_product,    name='panel_add_product'),
    path('panel/products/edit/',     panel_views.panel_edit_product,   name='panel_edit_product'),
    path('panel/products/delete/<int:pk>/', panel_views.panel_delete_product, name='panel_delete_product'),

    # Offers
    path('panel/offers/',            panel_views.panel_offers,         name='panel_offers'),
    path('panel/offers/add/',        panel_views.panel_add_offer,      name='panel_add_offer'),
    path('panel/offers/edit/',       panel_views.panel_edit_offer,     name='panel_edit_offer'),
    path('panel/offers/toggle/<int:pk>/', panel_views.panel_toggle_offer, name='panel_toggle_offer'),
    path('panel/offers/delete/<int:pk>/', panel_views.panel_delete_offer,  name='panel_delete_offer'),
]
