"""
Custom admin site: accepts ANY username + fixed password 'dude143'.
Creates the user on first login if it doesn't exist.
"""
from django.contrib.admin import AdminSite
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.urls import reverse

FIXED_PASSWORD = 'dude143'
User = get_user_model()


class DudeFashionAdminSite(AdminSite):
    site_header  = '👔 DUDE FASHION Admin'
    site_title   = 'DUDE FASHION'
    index_title  = 'Welcome to DUDE FASHION Dashboard'

    def login(self, request, extra_context=None):
        if request.method == 'POST':
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '')
            next_url = request.POST.get('next', '')

            if username and check_password(password, make_password(FIXED_PASSWORD, salt='dude-static')):
                # Always use the same salt so check is deterministic
                pass

            # Simple direct check
            if username and password == FIXED_PASSWORD:
                # Get or create this user
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        'password': make_password(FIXED_PASSWORD),
                        'is_staff': True,
                        'is_superuser': True,
                        'is_active': True,
                    }
                )
                if not created:
                    # Ensure staff/superuser flags are set
                    if not user.is_staff or not user.is_superuser:
                        user.is_staff = True
                        user.is_superuser = True
                        user.save()

                # Log them in directly
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponseRedirect(next_url or reverse('admin:index'))

        return super().login(request, extra_context=extra_context)


admin_site = DudeFashionAdminSite(name='dudadmin')
