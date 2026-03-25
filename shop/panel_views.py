from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product, Offer

PANEL_PASSWORD = 'dude143'


# ── Auth helpers ────────────────────────────────────────────────────────────

def panel_login_required(view_fn):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('panel_user'):
            return redirect('panel_login')
        return view_fn(request, *args, **kwargs)
    wrapper.__name__ = view_fn.__name__
    return wrapper


# ── Login / Logout ──────────────────────────────────────────────────────────

def panel_login(request):
    if request.session.get('panel_user'):
        return redirect('panel_dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        if username and password == PANEL_PASSWORD:
            request.session['panel_user'] = username
            return redirect('panel_dashboard')
        else:
            error = 'Invalid username or password. Please try again.'

    return render(request, 'panel/login.html', {'error': error})


@require_POST
def panel_logout(request):
    request.session.flush()
    return redirect('panel_login')


# ── Dashboard ───────────────────────────────────────────────────────────────

@panel_login_required
def panel_dashboard(request):
    return render(request, 'panel/dashboard.html', {
        'active': 'dash',
        'total_products':  Product.objects.count(),
        'active_products': Product.objects.filter(active=True).count(),
        'total_offers':    Offer.objects.count(),
        'active_offers':   Offer.objects.filter(active=True).count(),
        'recent_products': Product.objects.order_by('-created')[:6],
        'live_offers':     Offer.objects.filter(active=True)[:4],
    })


# ── Products ─────────────────────────────────────────────────────────────────

@panel_login_required
def panel_products(request):
    return render(request, 'panel/products.html', {
        'active': 'products',
        'products': Product.objects.all(),
    })


@panel_login_required
@require_POST
def panel_add_product(request):
    try:
        p = Product(
            name=request.POST['name'].strip(),
            category=request.POST['category'],
            sub=request.POST.get('sub', '').strip(),
            price=int(request.POST['price']),
            orig=int(request.POST['orig']),
            badge=request.POST.get('badge', 'NEW'),
            image_url=request.POST.get('image_url', '').strip(),
            active=request.POST.get('active') == '1',
            order=int(request.POST.get('order', 0)),
        )
        if 'image' in request.FILES:
            p.image = request.FILES['image']
        p.save()
        messages.success(request, f'✅ "{p.name}" added to the store!')
    except Exception as e:
        messages.error(request, f'Error adding product: {e}')
    return redirect('panel_products')


@panel_login_required
@require_POST
def panel_edit_product(request):
    p = get_object_or_404(Product, id=request.POST['id'])
    try:
        p.name      = request.POST['name'].strip()
        p.category  = request.POST['category']
        p.sub       = request.POST.get('sub', '').strip()
        p.price     = int(request.POST['price'])
        p.orig      = int(request.POST['orig'])
        p.badge     = request.POST.get('badge', 'NEW')
        p.image_url = request.POST.get('image_url', '').strip()
        p.active    = request.POST.get('active') == '1'
        p.order     = int(request.POST.get('order', 0))
        if 'image' in request.FILES:
            p.image = request.FILES['image']
        p.save()
        messages.success(request, f'✅ "{p.name}" updated successfully!')
    except Exception as e:
        messages.error(request, f'Error updating product: {e}')
    return redirect('panel_products')


@panel_login_required
@require_POST
def panel_delete_product(request, pk):
    p = get_object_or_404(Product, id=pk)
    name = p.name
    p.delete()
    messages.success(request, f'🗑️ "{name}" deleted.')
    return redirect('panel_products')


# ── Offers ───────────────────────────────────────────────────────────────────

@panel_login_required
def panel_offers(request):
    return render(request, 'panel/offers.html', {
        'active': 'offers',
        'offers': Offer.objects.all(),
    })


@panel_login_required
@require_POST
def panel_add_offer(request):
    try:
        o = Offer(
            title=request.POST['title'].strip(),
            subtitle=request.POST.get('subtitle', '').strip(),
            discount=request.POST['discount'].strip(),
            code=request.POST.get('code', '').strip().upper(),
            active=request.POST.get('active') == '1',
        )
        o.save()
        messages.success(request, f'🎁 Offer "{o.title}" published!')
    except Exception as e:
        messages.error(request, f'Error adding offer: {e}')
    return redirect('panel_offers')


@panel_login_required
@require_POST
def panel_edit_offer(request):
    o = get_object_or_404(Offer, id=request.POST['id'])
    try:
        o.title    = request.POST['title'].strip()
        o.subtitle = request.POST.get('subtitle', '').strip()
        o.discount = request.POST['discount'].strip()
        o.code     = request.POST.get('code', '').strip().upper()
        o.active   = request.POST.get('active') == '1'
        o.save()
        messages.success(request, f'✅ Offer "{o.title}" updated!')
    except Exception as e:
        messages.error(request, f'Error updating offer: {e}')
    return redirect('panel_offers')


@panel_login_required
@require_POST
def panel_toggle_offer(request, pk):
    o = get_object_or_404(Offer, id=pk)
    o.active = not o.active
    o.save()
    status = 'activated' if o.active else 'paused'
    messages.success(request, f'{"▶" if o.active else "⏸"} Offer "{o.title}" {status}.')
    return redirect('panel_offers')


@panel_login_required
@require_POST
def panel_delete_offer(request, pk):
    o = get_object_or_404(Offer, id=pk)
    title = o.title
    o.delete()
    messages.success(request, f'🗑️ Offer "{title}" deleted.')
    return redirect('panel_offers')
